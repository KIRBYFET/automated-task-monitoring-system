from pydantic import BaseModel, Field
from typing import Optional, Literal

TaskStatus = Literal["PENDING", "DONE", "OVERDUE"]
TaskPriority = Literal["LOW", "MEDIUM", "HIGH"]

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=500)
    due_at: Optional[str] = None
    source: Optional[str] = Field(default="manual", max_length=50)
    external_id: Optional[str] = Field(default=None, max_length=50)
    priority: Optional[TaskPriority] = "MEDIUM"

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    description: Optional[str] = Field(default=None, max_length=500)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_at: Optional[str] = None
    source: Optional[str] = Field(default=None, max_length=50)
    external_id: Optional[str] = Field(default=None, max_length=50)

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]

    status: TaskStatus
    priority: TaskPriority

    due_at: Optional[str]
    overdue_at: Optional[str]

    source: str
    external_id: Optional[str]

    created_at: str
    updated_at: str

class OverdueReportOut(BaseModel):
    generated_at: str
    total_overdue: int
    by_priority: dict[str, int]
    items: list[TaskOut]