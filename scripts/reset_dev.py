from __future__ import annotations

import argparse
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "tasks.db"
LOG_DIR = PROJECT_ROOT / "automation" / "logs"


def delete_file(path: Path) -> bool:
    if path.exists() and path.is_file():
        path.unlink()
        return True
    return False


def delete_logs(log_dir: Path) -> int:
    if not log_dir.exists() or not log_dir.is_dir():
        return 0

    deleted = 0
    # Borra solo archivos .log (seguro)
    for p in log_dir.glob("*.log"):
        try:
            p.unlink()
            deleted += 1
        except Exception as e:
            print(f"[warn] Could not delete {p.name}: {e}")

    # Si queda vacío, elimina la carpeta
    try:
        if not any(log_dir.iterdir()):
            log_dir.rmdir()
    except Exception:
        pass

    return deleted


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Reset dev artifacts: delete SQLite DB and automation logs."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Do not ask for confirmation.",
    )
    parser.add_argument(
        "--keep-logs",
        action="store_true",
        help="Keep logs (only delete tasks.db).",
    )
    parser.add_argument(
        "--keep-db",
        action="store_true",
        help="Keep DB (only delete logs).",
    )

    args = parser.parse_args()

    to_delete_db = not args.keep_db
    to_delete_logs = not args.keep_logs

    print("=== Reset Dev ===")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"DB path:      {DB_PATH} {'(will delete)' if to_delete_db else '(keep)'}")
    print(f"Logs dir:     {LOG_DIR} {'(will delete *.log)' if to_delete_logs else '(keep)'}")

    if not args.force:
        confirm = input("Proceed? Type 'yes' to continue: ").strip().lower()
        if confirm != "yes":
            print("Aborted.")
            return

    deleted_db = delete_file(DB_PATH) if to_delete_db else False
    deleted_logs = delete_logs(LOG_DIR) if to_delete_logs else 0

    print("\n=== Result ===")
    print(f"DB deleted: {deleted_db}")
    print(f"Log files deleted: {deleted_logs}")
    print("Done.")


if __name__ == "__main__":
    main()
