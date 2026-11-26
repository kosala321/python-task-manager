import pytest
from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_tasks(monkeypatch):
    monkeypatch.setattr(main, "tasks", [])
    monkeypatch.setattr(main, "next_task_id", 1)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "Welcome to Task Manager API"
    )


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn Python"}
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn Python"
    assert response.json()["completed"] is False


def test_get_tasks():
    client.post("/tasks", json={"title": "Learn Git"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_complete_task():
    created = client.post(
        "/tasks",
        json={"title": "Learn GitHub"}
    )

    task_id = created.json()["id"]

    response = client.patch(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_task():
    created = client.post(
        "/tasks",
        json={"title": "Delete me"}
    )

    task_id = created.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"


def test_missing_task():
    response = client.patch("/tasks/999")

    assert response.status_code == 404
