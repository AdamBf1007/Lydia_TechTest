import requests
import pytest

url = "https://reqres.in/api"
key = {"x-api-key": "reqres-free-v1"}


def test_register_user():
    # POST - /register
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(
        f"{url}/register",
        json=payload,
        headers=key
    )

    print(response.status_code)
    print(response.text)

   
    assert response.status_code == 200

  
    data = response.json()
    assert "id" in data
    assert "token" in data


def test_get_user():
    # GET - /users/{id}
    user_id = 2

    response = requests.get(
        f"{url}/users/{user_id}",
        headers=key
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    data = response.json()
    assert data["data"]["id"] == user_id
    assert "email" in data["data"]
