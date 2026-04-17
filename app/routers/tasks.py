from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from app import services

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return services.create_task(db, task)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    sort_by: Optional[str] = Query(None, pattern="^(title|status|created_at|priority)$"),
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return services.get_tasks(db, sort_by=sort_by, search=search)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = services.get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    task = services.update_task(db, task_id, task_data)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted = services.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}


@router.get("/top/{n}", response_model=list[TaskResponse])
def get_top_priority_tasks(n: int, db: Session = Depends(get_db)):
    return services.get_top_priority_tasks(db, n)