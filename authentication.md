# Authentication in FastAPI

<br>

> ### Step By Step

<br>

1. pip3 install python-multipart
2. from fastapi.security import OAuth2PasswordRequestForm
3. form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
4. Function for user authentication:
```python
    def authenticate_user(username: str, password: str, db):
        user = db.query(Users).filter(Users.username == username).first()
        if not user:
            return False
        if not bcrypt_context.verify(password, user.hashed_password):
            return False
        return True
```