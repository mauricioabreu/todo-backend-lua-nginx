import requests


def test_create_todo():
    response = requests.post(
        "http://api:80/todos", json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy some groceries"
    assert data["completed"] == False


def test_delete_todo():
    response = requests.post(
        "http://api:80/todos", json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()

    response = requests.delete(f"http://api:80/todos/{data['id']}")
    assert response.status_code == 204


def test_get_todo():
    response = requests.post(
        "http://api:80/todos", json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()

    response = requests.get(f"http://api:80/todos/{data['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy some groceries"


def test_list_todos():
    requests.post("http://api:80/flush")

    response = requests.post(
        "http://api:80/todos", json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    response = requests.post("http://api:80/todos", json={"title": "do homework"})
    assert response.status_code == 200

    response = requests.get("http://api:80/todos")
    data = response.json()
    assert len(data) == 2


def test_update_nonexistent_todo():
    response = requests.patch(f"http://api:80/todos/1", json={"title": "do homework"})
    assert response.status_code == 404


def test_update_todo():
    response = requests.post(
        "http://api:80/todos", json={"title": "buy some groceries"}
    )
    assert response.status_code == 200
    data = response.json()

    response = requests.patch(
        f"http://api:80/todos/{data['id']}",
        json={"title": "do homework", "completed": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "do homework"
