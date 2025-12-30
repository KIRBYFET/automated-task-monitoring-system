import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "tasks.db"

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,

            status TEXT NOT NULL CHECK(status IN ('PENDING','DONE','OVERDUE')) DEFAULT 'PENDING',
            priority TEXT NOT NULL CHECK(priority IN ('LOW','MEDIUM','HIGH')) DEFAULT 'MEDIUM',

            due_at TEXT,
            overdue_at TEXT,

            source TEXT NOT NULL DEFAULT 'manual',
            external_id TEXT,

            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        """)
        conn.commit()