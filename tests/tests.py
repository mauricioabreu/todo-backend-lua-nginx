from urllib import response
import requests


def test_create_todo():
    response = requests.post("http://api:80/todos", data={"title": "buy some groceries"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy some groceries"