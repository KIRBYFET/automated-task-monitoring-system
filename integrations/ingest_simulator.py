import os
import time
import random
from datetime import datetime, timedelta, timezone
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
INTERVAL_SECONDS = int(os.getenv("SIM_INTERVAL_SECONDS", "8"))
SEED = os.getenv("SIM_SEED")  # opcional

CREATE_PROB = float(os.getenv("SIM_CREATE_PROB", "0.70"))

TEMPLATES = [
    ("Verify daily backups", "Confirm backups completed successfully."),
    ("Rotate application logs", "Archive and rotate logs to prevent disk issues."),
    ("Renew SSL certificate", "Renew/replace SSL before expiration."),
    ("Update OS packages", "Apply security patches on staging servers."),
    ("Check disk usage", "Investigate partitions above threshold."),
    ("Validate monitoring alerts", "Review recent alerts and close false positives."),
]

def iso_utc(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()

def make_due_at() -> str:
    now = datetime.now(timezone.utc)
    if random.random() < 0.35:
        dt = now - timedelta(minutes=random.randint(10, 120))
    else:
        dt = now + timedelta(minutes=random.randint(30, 240))
    return iso_utc(dt)

def api_post(path: str, payload: dict) -> dict:
    r = requests.post(f"{BASE_URL}{path}", json=payload, timeout=10)
    r.raise_for_status()
    return r.json()

def api_get(path: str, params: dict | None = None):
    r = requests.get(f"{BASE_URL}{path}", params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def api_patch(path: str, payload: dict) -> dict:
    r = requests.patch(f"{BASE_URL}{path}", json=payload, timeout=10)
    r.raise_for_status()
    return r.json()

def create_task() -> dict:
    title, description = random.choice(TEMPLATES)
    external_id = f"OPS-{random.randint(1000, 9999)}"
    priority = random.choices(["LOW", "MEDIUM", "HIGH"], weights=[2, 6, 2])[0]

    payload = {
        "title": title,
        "description": description,
        "due_at": make_due_at(),
        "source": "simulator",
        "external_id": external_id,
        "priority": priority,
    }
    return api_post("/tasks", payload)

def pick_close_candidate():
    pending_sim = api_get("/tasks", params={"status": "PENDING", "source": "simulator"})
    if pending_sim:
        return random.choice(pending_sim)

    pending_any = api_get("/tasks", params={"status": "PENDING"})
    if pending_any:
        return random.choice(pending_any)

    return None

def close_task(task: dict) -> dict:
    return api_patch(f"/tasks/{task['id']}", {"status": "DONE"})

def main():
    if SEED:
        random.seed(int(SEED))

    print(f"[simulator] base url: {BASE_URL}")
    print(f"[simulator] interval: {INTERVAL_SECONDS}s")
    print(f"[simulator] create_prob: {CREATE_PROB:.2f} close_prob: {1.0-CREATE_PROB:.2f}")

    while True:
        try:
            do_create = random.random() < CREATE_PROB

            if do_create:
                task = create_task()
                print(f"[simulator] CREATE  id={task['id']} title={task['title']} due_at={task.get('due_at')} prio={task.get('priority')} ext={task.get('external_id')}")
            else:
                candidate = pick_close_candidate()
                if not candidate:
                    task = create_task()
                    print(f"[simulator] CREATE  id={task['id']} title={task['title']} (no pending to close)")
                else:
                    updated = close_task(candidate)
                    print(f"[simulator] CLOSE   id={updated['id']} title={updated['title']} status={updated['status']} source={updated.get('source')} ext={updated.get('external_id')}")

        except Exception as e:
            print(f"[simulator] error: {e}")

        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
