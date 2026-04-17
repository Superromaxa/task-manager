from typing import Optional

from sqlalchemy.orm import Session

from .models import TaskModel
from .schemas import TaskCreate, TaskUpdate


def create_task(db: Session, task_data: TaskCreate) -> TaskModel:
    task = TaskModel(**task_data.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(
    db: Session,
    sort_by: Optional[str] = None,
    search: Optional[str] = None
) -> list[TaskModel]:
    query = db.query(TaskModel)

    if search:
        query = query.filter(
            (TaskModel.title.ilike(f"%{search}%")) |
            (TaskModel.description.ilike(f"%{search}%"))
        )

    if sort_by in {"title", "status", "created_at", "priority"}:
        query = query.order_by(getattr(TaskModel, sort_by))

    return query.all()


def get_task_by_id(db: Session, task_id: int) -> TaskModel | None:
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> TaskModel | None:
    task = get_task_by_id(db, task_id)
    if task is None:
        return None

    for field, value in task_data.model_dump().items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int) -> bool:
    task = get_task_by_id(db, task_id)
    if task is None:
        return False

    db.delete(task)
    db.commit()
    return True


def get_top_priority_tasks(db: Session, n: int) -> list[TaskModel]:
    return db.query(TaskModel).order_by(TaskModel.priority.desc()).limit(n).all()   