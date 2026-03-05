import pytest
from jsonschema import validate
from utils.schemas import USER_LIST_SCHEMA, USER_SCHEMA, CREATE_USER_SCHEMA


class TestGetUsers:
    def test_get_user_list_returns_200(self, api):
        response = api.get("/users", params={"page": 1})
        assert response.status_code == 200

    def test_get_user_list_returns_6_users_per_page(self, api):
        response = api.get("/users", params={"page": 1})
        assert len(response.json()["data"]) == 6

    def test_get_single_user_returns_200(self, api):
        response = api.get("/users/2")
        assert response.status_code == 200

    def test_get_single_user_has_correct_id(self, api):
        response = api.get("/users/2")
        assert response.json()["data"]["id"] == 2

    def test_get_nonexistent_user_returns_404(self, api):
        response = api.get("/users/9999")
        assert response.status_code == 404

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
    def test_multiple_users_return_200(self, api, user_id):
        response = api.get(f"/users/{user_id}")
        assert response.status_code == 200


class TestCreateUser:
    def test_create_user_returns_201(self, api):
        response = api.post("/users", json={"name": "Luis", "job": "QA Engineer"})
        assert response.status_code == 201

    def test_create_user_returns_correct_name(self, api):
        response = api.post("/users", json={"name": "Luis", "job": "QA Engineer"})
        assert response.json()["name"] == "Luis"

    def test_create_user_response_has_id(self, api):
        response = api.post("/users", json={"name": "Luis", "job": "QA"})
        assert "id" in response.json()


class TestUpdateUser:
    def test_update_user_returns_200(self, api):
        response = api.put("/users/2", json={"name": "Luis", "job": "Senior QA"})
        assert response.status_code == 200

    def test_update_user_response_has_updated_at(self, api):
        response = api.put("/users/2", json={"name": "Luis", "job": "QA"})
        assert "updatedAt" in response.json()


class TestDeleteUser:
    def test_delete_user_returns_204(self, api):
        response = api.delete("/users/2")
        assert response.status_code == 204
