import pytest
from users.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_user_create_success():
    client = APIClient()
    payload = {
        "email": "testuser@yandex.ru",
        "password": "supersecure123",
        "last_name": "test",
        "first_name": "test"
    }

    response = client.post("/users/register/", payload, format="json")

    print(response)

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "testuser@yandex.ru"

    user = User.objects.get(email="testuser@yandex.ru")
    assert user.check_password("supersecure123")