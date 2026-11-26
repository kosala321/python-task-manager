from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task Manager API",
    description="A beginner-friendly Python API",
    version="1.0.0"
)

tasks = []
next_task_id = 1


class TaskCreate(BaseModel):
    title: str


@app.get("/")
def home():
    return {"message": "Welcome to Task Manager API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_task_id

    new_task = {
        "id": next_task_id,
        "title": task.title,
        "completed": False
    }

    tasks.append(new_task)
    next_task_id += 1

    return new_task


@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
