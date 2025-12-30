import os
import time
from pathlib import Path
from datetime import datetime, timezone, timedelta
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
INTERVAL_SECONDS = int(os.getenv("RUNNER_INTERVAL_SECONDS", "10"))
ESCALATE_AFTER_MINUTES = int(os.getenv("ESCALATE_AFTER_MINUTES", "30"))

LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def parse_iso(dt_str: str):
    if not dt_str:
        return None
    try:
        return datetime.fromisoformat(dt_str.replace("Z", "+00:00"))
    except Exception:
        return None

def now_utc():
    return datetime.now(timezone.utc)

def is_past(dt_str: str) -> bool:
    dt = parse_iso(dt_str)
    if not dt:
        return False
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt < now_utc()

def list_tasks(params: dict) -> list[dict]:
    r = requests.get(f"{BASE_URL}/tasks", params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def patch_task(task_id: int, fields: dict) -> dict:
    r = requests.patch(f"{BASE_URL}/tasks/{task_id}", json=fields, timeout=10)
    r.raise_for_status()
    return r.json()

def write_log(lines: list[str]) -> Path:
    today = now_utc().date().isoformat()
    path = LOG_DIR / f"automation_{today}.log"
    with path.open("a", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    return path

def main():
    print(f"[runner] base url: {BASE_URL}")
    print(f"[runner] interval: {INTERVAL_SECONDS}s")
    print(f"[runner] escalate after: {ESCALATE_AFTER_MINUTES} minutes overdue")

    while True:
        lines = []
        try:
            pending = list_tasks({"status": "PENDING"})
            overdue_candidates = [t for t in pending if t.get("due_at") and is_past(t["due_at"])]

            marked = 0
            for t in overdue_candidates:
                try:
                    patch_task(t["id"], {"status": "OVERDUE"})
                    marked += 1
                except Exception as e:
                    lines.append(f"! failed_mark_overdue id={t['id']} error={e}")

            overdue = list_tasks({"status": "OVERDUE"})
            escalated = 0
            threshold = now_utc() - timedelta(minutes=ESCALATE_AFTER_MINUTES)

            for t in overdue:
                if t.get("priority") == "HIGH":
                    continue
                od_at = parse_iso(t.get("overdue_at"))
                if not od_at:
                    continue
                if od_at.tzinfo is None:
                    od_at = od_at.replace(tzinfo=timezone.utc)

                if od_at < threshold:
                    try:
                        patch_task(t["id"], {"priority": "HIGH"})
                        escalated += 1
                    except Exception as e:
                        lines.append(f"! failed_escalate id={t['id']} error={e}")

            ts = now_utc().replace(microsecond=0).isoformat()
            header = f"time_utc={ts} pending={len(pending)} newly_overdue={len(overdue_candidates)} marked_overdue={marked} total_overdue={len(overdue)} escalated_to_high={escalated}"
            print("[runner]", header)
            lines.insert(0, header)

            if len(overdue_candidates) > 0 or escalated > 0:
                lines.append("details:")
                for t in overdue_candidates[:10]:
                    lines.append(f"- newly_overdue id={t['id']} title={t['title']} due_at={t.get('due_at')} priority={t.get('priority')} source={t.get('source')} ext={t.get('external_id')}")
                log_path = write_log(lines)
                print(f"[runner] log appended: {log_path}")

        except Exception as e:
            print(f"[runner] error: {e}")

        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
