# Domain-driven Architecture in Python

## Why?

Check the [Kotlin version readme](https://github.com/lsoares/clean-architecture-sample).

## Commands
- Setup: get [Poetry](https://python-poetry.org) and `poetry install`
- Run app: `uvicorn web.main:app`
- Run tests: `pytest`


## Challenge
1 - let's prevent repeated emails:
```python
def test_cant_create_repeated_user():
    client = TestClient(WebApp(user_repository=UserRepositoryInMemory()))
    _create_user(client, "luis.s@gmail.com", "Luís Soares", "password")

    response = _create_user(client, "luis.s@gmail.com", "Luís Soares", "password")

    assert response.status_code == 409
    assert _list_users(client).json() == [
        {"name": "Luís Soares", "email": "luis.s@gmail.com"}
    ]
```
2 - let's allow deleting a user:
```python

```
