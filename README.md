# API Testing Framework — ReqRes API

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white) ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) ![Requests](https://img.shields.io/badge/Requests-2.x-orange?style=flat-square) ![Tests](https://img.shields.io/badge/Tests-50%2B-brightgreen?style=flat-square)

Automated REST API testing framework using Python + Pytest + Requests. Covers CRUD operations on the [ReqRes](https://reqres.in) public API with schema validation and HTML reports.

## 🎯 What This Project Demonstrates

- Automated API test coverage using **Pytest** and **Requests**
- **JSON Schema validation** for response structure verification
- **CRUD operations**: GET, POST, PUT, DELETE
- **HTML test reports** generated with pytest-html
- Clean project structure following QA best practices

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Main language |
| Pytest | Latest | Test framework |
| Requests | 2.x | HTTP client |
| pytest-html | Latest | HTML reports |
| jsonschema | Latest | Schema validation |

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/luiselizondotech-dotcom/api-testing-framework-python

# Install dependencies
pip install -r requirements.txt

# Run all tests with HTML report
pytest --html=reports/report.html -v
```

## 📋 Test Coverage

| Endpoint | Operations | Tests |
|----------|-----------|-------|
| `GET /users` | List, single user, not found | 8+ tests |
| `POST /users` | Create and validate response | 5+ tests |
| `PUT /users` | Update user | 5+ tests |
| `DELETE /users` | Delete user | 4+ tests |
| `POST /login` | Valid credentials, missing fields | 6+ tests |
| `POST /register` | Success and error handling | 5+ tests |

## 📊 Results

- ✅ 50+ automated test cases
- ✅ HTML reports generated on every run
- ✅ Schema validation for all responses
- ✅ Full CRUD coverage

## 👤 Author

**Luis Elizondo** — QA Engineer
- GitHub: [@luiselizondotech-dotcom](https://github.com/luiselizondotech-dotcom)
- LinkedIn: [qa-engineer-elizondo-luis](https://www.linkedin.com/in/qa-engineer-elizondo-luis)
- Portfolio: [luis-qa-journey.lovable.app](https://luis-qa-journey.lovable.app)
