import pytest
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def api():
    """Base API client fixture available for all tests."""
    return APIClient(base_url="https://reqres.in/api")


@pytest.fixture(scope="session")
def auth_token(api):
    """Fixture that returns a valid auth token."""
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = api.post("/login", json=payload)
    return response.json().get("token")
