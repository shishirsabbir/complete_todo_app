# Password hashing in FastAPI

<br>

> ### Step By Step:

<br>

1. pip3 install "passlib[bcrypt]"
2. from passlib.context import CryptContext
3. bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
4. hashed_password = bcrypt_context.hash(create_user_request.password)