from datetime import datetime, timezone, timedelta
from typing import Optional, List
from .db import get_conn

def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def create_task(title, description, due_at, source, external_id, priority) -> dict:
    ts = now_iso()
    with get_conn() as conn:
        cur = conn.execute(
            """
            INSERT INTO tasks (title, description, status, priority, due_at, overdue_at, source, external_id, created_at, updated_at)
            VALUES (?, ?, 'PENDING', ?, ?, NULL, ?, ?, ?, ?)
            """,
            (title, description, priority, due_at, source, external_id, ts, ts),
        )
        task_id = cur.lastrowid
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return dict(row)

def list_tasks(status: Optional[str] = None, source: Optional[str] = None, priority: Optional[str] = None) -> List[dict]:
    q = "SELECT * FROM tasks"
    clauses = []
    params = []

    if status is not None:
        clauses.append("status = ?")
        params.append(status)
    if source is not None:
        clauses.append("source = ?")
        params.append(source)
    if priority is not None:
        clauses.append("priority = ?")
        params.append(priority)

    if clauses:
        q += " WHERE " + " AND ".join(clauses)

    q += " ORDER BY id DESC"

    with get_conn() as conn:
        rows = conn.execute(q, params).fetchall()
        return [dict(r) for r in rows]

def get_task(task_id: int) -> Optional[dict]:
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
        return dict(row) if row else None

def update_task(task_id: int, title=None, description=None, status=None, priority=None, due_at=None, source=None, external_id=None) -> Optional[dict]:
    existing = get_task(task_id)
    if not existing:
        return None

    new_title = title if title is not None else existing["title"]
    new_description = description if description is not None else existing["description"]
    new_status = status if status is not None else existing["status"]
    new_priority = priority if priority is not None else existing["priority"]
    new_due_at = due_at if due_at is not None else existing["due_at"]
    new_source = source if source is not None else existing["source"]
    new_external_id = external_id if external_id is not None else existing["external_id"]

    new_overdue_at = existing["overdue_at"]
    if existing["status"] != "OVERDUE" and new_status == "OVERDUE":
        new_overdue_at = now_iso()
    if new_status == "PENDING":
        new_overdue_at = None

    with get_conn() as conn:
        conn.execute(
            """
            UPDATE tasks
               SET title = ?, description = ?, status = ?, priority = ?, due_at = ?, overdue_at = ?, source = ?, external_id = ?, updated_at = ?
             WHERE id = ?
            """,
            (new_title, new_description, new_status, new_priority, new_due_at, new_overdue_at, new_source, new_external_id, now_iso(), task_id),
        )
        conn.commit()

    return get_task(task_id)

def delete_task(task_id: int) -> bool:
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cur.rowcount > 0