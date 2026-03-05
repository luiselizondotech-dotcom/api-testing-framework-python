import requests


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "x-api-key": "reqres_1d4a7ea85e0a4112a0dc16ed7f843e15"
})

    def get(self, endpoint: str, params: dict = None) -> requests.Response:
        return self.session.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint: str, json: dict = None) -> requests.Response:
        return self.session.post(f"{self.base_url}{endpoint}", json=json)

    def put(self, endpoint: str, json: dict = None) -> requests.Response:
        return self.session.put(f"{self.base_url}{endpoint}", json=json)

    def delete(self, endpoint: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}{endpoint}")
