# JWT

<br>

> ### JSON Web Token Structure

A JSON Web Token is created of three separate parts separated by dots(.) which includes:
1. Header (a)
2. Payload (b)
3. Signature (c)

```json
aaaaaaaaaa.bbbbbbbbbb.ccccccccccc
```
<br>

**JWT Header**
JWT Header usually consist of two parts:
1. alg (The algorithm for signin)
2. typ (The specific type of token)

*JWT header is then encoded using base64 to create the first part of the JWT(a)*

<br>

**JWT Payload- Second part of JSON Web Token**

A JWT payload consists of the data. Payloads data contains claims, and there are three different types of claims.
1. Registered Claims
2. Public Claims
3. Private Claims

**Registered Claims**
Registered claims are claims that are predefined, recommended but not mandatory.
The top 3 registered claims includes *ISS*, *SUB* and *EXP*.

- ISS stands for Issuer: This claim identifies the principal that issued the JWT.
- SUB stands for Subject: It holds statements about the subject. The subject value must be scoped either locally or globally unique. Think of a subject as an ID for the JWT.
- EXP stands for Expiration time: It holds when the JWT will expire. This claim makes sure that the current date and time is before the expiration date and time of the token. Expiration is not mandatory but extremely useful.



<br>

**JWT Signature**
The third and final part of the JWT. A JWT Signature is created by using the algorithm in the header to hash out
the encoded header, encoded payload and secret. The secret can be anything but somewhere on the server that the
client does not have access to.

<br>
<br>


### Return a JWT

<br>

> **Step By Step:**
1. ```pip3 install "python-jose[cryptography]"```
2. ```from jose import jwt```
3. Create a secret key

```bash
openssl rand -hex 32
```

```python
SECRET_KEY = "6ecee6c2db210f556c610d1936e5e4dc41a6428d2e9de149a1f409cb18e1d37b"
ALGORITHM = "HS256"
```

4. Function for creating access token

```python
# function for creating access token
def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": user_id}
    expires = datetime.utcnow() + expires_delta

    encode.update({"exp": expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
```

5. Return token response

```python
@router.post('/token', response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        return "Failed Authentication"
    
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}
```