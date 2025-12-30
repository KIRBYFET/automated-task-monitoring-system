from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
from datetime import datetime, timezone

from .db import init_db
from .schemas import TaskCreate, TaskUpdate, TaskOut, TaskStatus, TaskPriority, OverdueReportOut
from . import crud

app = FastAPI(title="Automated Task Monitoring System")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks", response_model=TaskOut)
def create_task(payload: TaskCreate):
    return crud.create_task(
        payload.title,
        payload.description,
        payload.due_at,
        payload.source or "manual",
        payload.external_id,
        payload.priority or "MEDIUM",
    )

@app.get("/tasks", response_model=List[TaskOut])
def list_tasks(
    status: Optional[TaskStatus] = Query(default=None),
    source: Optional[str] = Query(default=None),
    priority: Optional[TaskPriority] = Query(default=None),
):
    return crud.list_tasks(status=status, source=source, priority=priority)

@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    row = crud.get_task(task_id)
    if not row:
        raise HTTPException(404, "Task not found")
    return row

@app.patch("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate):
    row = crud.update_task(
        task_id,
        title=payload.title,
        description=payload.description,
        status=payload.status,
        priority=payload.priority,
        due_at=payload.due_at,
        source=payload.source,
        external_id=payload.external_id,
    )
    if not row:
        raise HTTPException(404, "Task not found")
    return row

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    ok = crud.delete_task(task_id)
    if not ok:
        raise HTTPException(404, "Task not found")
    return {"deleted": True, "id": task_id}

@app.get("/reports/overdue", response_model=OverdueReportOut)
def overdue_report(priority: Optional[TaskPriority] = Query(default=None)):
    items = crud.list_tasks(status="OVERDUE", priority=priority)
    by_priority = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
    for t in items:
        by_priority[t["priority"]] = by_priority.get(t["priority"], 0) + 1

    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "total_overdue": len(items),
        "by_priority": by_priority,
        "items": items,
    }