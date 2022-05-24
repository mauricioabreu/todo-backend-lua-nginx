from urllib import response
import requests


def test_create_todo():
    response = requests.post("http://api:80/todos", json={"title": "buy some groceries"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy some groceries"

def test_delete_todo():
    response = requests.post("http://api:80/todos", json={"title": "buy some groceries"})
    assert response.status_code == 200
    data = response.json()

    response = requests.delete(f"http://api:80/todos/{data['uid']}")
    assert response.status_code == 204

def test_get_todo():
    response = requests.post("http://api:80/todos", json={"title": "buy some groceries"})
    assert response.status_code == 200
    data = response.json()

    response = requests.get(f"http://api:80/todos/{data['uid']}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy some groceries"