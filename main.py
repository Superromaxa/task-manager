from fastapi import FastAPI

from .database import Base, engine
from .routers.tasks import router as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")


@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}


app.include_router(tasks_router)