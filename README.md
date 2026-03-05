# API Testing Framework - ReqRes API

Automated REST API testing framework using Python + Pytest + Requests.

## Tech Stack
- Python 3.10+
- Pytest
- Requests
- pytest-html
- jsonschema

## Getting Started
1. pip install -r requirements.txt
2. pytest --html=reports/report.html -v

## Test Coverage
- GET /users - list, single user, not found
- POST /users - create and validate response
- PUT /users - update user
- DELETE /users - delete user
- POST /login - valid credentials, missing fields
- POST /register - success and error handling

## Author
Luis Elizondo - QA Engineer
GitHub: https://github.com/luiselizondotech-dotcom
