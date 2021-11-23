# Domain-driven Architecture in Python

## Why?

Check the [Kotlin version readme](https://github.com/lsoares/clean-architecture-sample).

## Commands
- Setup: get [Poetry](https://python-poetry.org) and `poetry install`
- Run app: `uvicorn web.main:app`
- Run tests: `pytest`


## Challenge
1. Let's prevent repeated emails:
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
2. Why do we need a mapper in `ListUsersHandler`? Why do we need a DTO in `CreateUser` use case?
3. What would you do to create/use an alternative `UserRepository`?
4. Why do we need a `UserRepository` interface?
5. Let's allow deleting a user:
    ```python
    def test_delete_a_user():
        client = TestClient(WebApp(user_repository=UserRepositoryInMemory()))
        _create_user(client, "luis.s@gmail.com", "Luís Soares", "password")
        _create_user(client, "miguel.s@gmail.com", "Miguel Soares", "password")
    
        response = _delete_user(client, "luis.s@gmail.com")
        
        assert response.status_code == 204
        assert _list_users(client).json() == [
            {"name": "Miguel Soares", "email": "miguel.s@gmail.com"}
        ]
    
    def _delete_user(client, email: str):
        return client.delete(url=f"/users/{email}")
    ```
6. Why do we only test "as a user"? Don't we create domain tests? What's the trade-off?
7. Can you list what the domain contains?
8. What does a port mean? What does it contain?
9. Why is `web` outside of `adapters`? Where would you put a CLI or a worker/job?
10. Why is `main.py` under `web`?
11. Let's create a DSL for test usage
