# Domain-driven Architecture in Python

## Why?

Check the [Kotlin version readme](https://github.com/lsoares/clean-architecture-sample).

## Commands

- Setup: get [Poetry](https://python-poetry.org) and `poetry install`
- Run app: `uvicorn web.main:app`
- Run tests: `poetry run pytest`

## Challenge

1. The Grinch has secretly broken the code and the tests are not passing...
2. What are the uses cases, entities and ports? What are the primary adapters? And secondary?\
   _use cases: createuser, listusers / entities: user ports: userrepository / primary adapters: web / secondary
   adapters: UserRepositoryInMemory_
3. Let's prevent repeated emails. Here's the test:
    ```python
    def test_cant_create_repeated_user():
        client = TestClient(WebApp(user_repository=UserRepositoryInMemory()))
        _create_user(client, "jake.jackson@fbi.gov", "Jake Jackson", "password")
    
        response = _create_user(client, "jake.jackson@fbi.gov", "Jake Jackson", "password")
    
        assert response.status_code == 409
        assert _list_users(client).json() == [
            {"name": "Jake Jackson", "email": "jake.jackson@fbi.gov"}
        ]
    ```
4. Where did you write the error class and why?\
   _it belongs to UserRepository port because then any of its implementations can throw it._
5. What does a port mean? What does it contain?A port is an abstraction of a secondary repository.\
   _it contains its interface, DTOs (request/response models) and possible errors._
6. What's the advantage of the `UserRepository` port? What would you do to create and use an alternative
   to `UserRepositoryInMemory`?\
   _Abstracting the way we do User CRUD. We could create another implementation like UserRepoDatabase and inject it in
   main.py._
7. Let's allow deleting a user. Here's the test:
    ```python
    def test_delete_a_user():
        client = TestClient(WebApp(user_repository=UserRepositoryInMemory()))
        _create_user(client, "jake.jackson@fbi.gov", "Jake Jackson", "password")
        _create_user(client, "john.doe@gmail.com", "John Doe", "password")
    
        response = _delete_user(client, "jake.jackson@fbi.gov")
        
        assert response.status_code == 204
        assert _list_users(client).json() == [
            {"name": "John Doe", "email": "john.doe@gmail.com"}
        ]
    
    def _delete_user(client, email: str):
        return client.delete(url=f"/users/{email}")
    ```
8. Why do we only test "as a user"? Don't we create domain tests? What's the trade-off?\
   _To be more realistic; to avoid testing implementation details; to ease refactoring; to document the codebase
   abilities. The trade-off is that we loose a bit a pinpointing ability. Tests may be slower. We may need to do
   variations hitting the domain directly though._
9. Where would you put a CLI or a worker/job? In the root.\
   _Although they're adapters, they're primary adapters (i.e. entrypoints). That means they're the reason this app
   exists; therefore it's ok to give them highlight in the root folder._
10. Why is `main.py` under `web`?\
    _Because it's the booting and DI of the web app primary adapter (entrypoint). Other primary adapters would have
    their own booting/DI._
11. What are the upsides/downsides of having a use-case orientation? (separating use cases per file in the web and the
    domain)\
    _More files but more clarity on the abilities of the app. Less code sharing which good so that features become
    modular. It makes dependencies much more clear because each feature only has what it needs. Finally, less code
    hotspots._
12. Let's create a DSL for test usage (suggestion: create an `ApiClient` class and pass it the HTTP client).
