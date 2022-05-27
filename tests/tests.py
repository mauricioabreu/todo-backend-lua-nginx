import os
import requests


SITE_URL = "http://api:8080"
TODOS_ENDPOINT = f"{SITE_URL}/todos"


def test_create_todo():
    response = requests.post(
        TODOS_ENDPOINT, json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy some groceries"
    assert data["completed"] == False


def test_delete_todo():
    response = requests.post(
        TODOS_ENDPOINT, json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()

    response = requests.delete(f"{TODOS_ENDPOINT}/{data['id']}")
    assert response.status_code == 204


def test_get_todo():
    response = requests.post(
        TODOS_ENDPOINT, json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()

    response = requests.get(f"{TODOS_ENDPOINT}/{data['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy some groceries"


def test_list_todos():
    requests.post(f"{SITE_URL}/flush")

    response = requests.post(
       TODOS_ENDPOINT, json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    response = requests.post(TODOS_ENDPOINT, json={"title": "do homework"})
    assert response.status_code == 200

    response = requests.get(TODOS_ENDPOINT)
    data = response.json()
    assert len(data) == 2


def test_update_nonexistent_todo():
    response = requests.patch(f"{TODOS_ENDPOINT}/1", json={"title": "do homework"})
    assert response.status_code == 404


def test_update_todo():
    response = requests.post(
        TODOS_ENDPOINT, json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()

    response = requests.patch(
        f"{TODOS_ENDPOINT}/{data['id']}",
        json={"title": "do homework", "completed": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "do homework"
