class TestLogin:
    def test_login_valid_credentials_returns_200(self, api):
        payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = api.post("/login", json=payload)
        assert response.status_code == 200

    def test_login_returns_token(self, api):
        payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        response = api.post("/login", json=payload)
        assert "token" in response.json()

    def test_login_without_password_returns_400(self, api):
        response = api.post("/login", json={"email": "eve.holt@reqres.in"})
        assert response.status_code == 400

    def test_login_without_email_returns_400(self, api):
        response = api.post("/login", json={"password": "cityslicka"})
        assert response.status_code == 400


class TestRegister:
    def test_register_valid_data_returns_200(self, api):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = api.post("/register", json=payload)
        assert response.status_code == 200

    def test_register_response_has_token(self, api):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = api.post("/register", json=payload)
        assert "token" in response.json()

    def test_register_without_password_returns_400(self, api):
        response = api.post("/register", json={"email": "test@test.com"})
        assert response.status_code == 400
