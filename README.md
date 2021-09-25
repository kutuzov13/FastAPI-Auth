# FastAPI - JWT

An example of JWT authorization in conjunction with Deta.

## Tools

  - Python 3.8
  - [FastAPI](https://fastapi.tiangolo.com/)
  - [Deta Base(Base)](https://www.deta.sh/): database for our application
  - [pyJWT](https://pyjwt.readthedocs.io/en/latest/): library for encoding and decoding JWT tokens
  - [PassLib[BCrypt]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html): password hashing library

## Start

You need to get the  project key [Deta](https://www.deta.sh/) for use with Deta Base.
The base is used to store user account information such as username and hashed password.

Create a new project and make sure to save the key in a secure place!

Add the key to your environment variables or `.env` file like this `DETA_PROJECT_KEY=YOUR_COPIED_PROJECT_KEY`

To test the app, go to the terminal in the same directory and run `uvicorn main:app` or `python main.py`,
you can then go `/doc` on the local endpoint (http://127.0.0.1:8000/docs) to test the application.


# Example

`/signup`
```http request
curl -X 'POST' \
  'http://127.0.0.1:8000/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username",
  "password": "strongpassword"
}'

Response Body
{
  "key": "username",
  "password": "$2b$12$/Gq7g40zZ4/sQ9iWfqVze.Jx5HI5XwCrERITGG/wZivuZ9jhkd0bK"
}
```

`/login`
```http request
curl -X 'POST' \
  'http://127.0.0.1:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username",
  "password": "strongpassword"
}'

Response Body
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTgyNDE1MjAsImlhdCI6MTYxODIzOTcyMCwic3ViIjoiZmx5aW5nc3BvbmdlIn0.SoMeSo_b9z4fC-XnR8bepUbFvWvSEw9rRQ9LMJNzm3k"
}

```

`/secret`
```http request
curl -X 'POST' \
  'http://127.0.0.1:8000/secret' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTg5MzU3MzcsImlhdCI6MTYxODkzNTY3Nywic3ViIjoicm9oYW4ifQ.dja0E6SUaZfEvYVKySjLE9OLXOtob5pjpy3R_rlCD7c' \
  -d ''

Response body
"Top Secret data only authorized users can access this info"

```

`/notsecret`
```http request
curl -X 'GET' \
  'http://127.0.0.1:8000/notsecret' \
  -H 'accept: application/json'

Response Body
"Not secret data"
```


`/refresh_token`
```http request
curl -X 'GET' \
  'http://127.0.0.1:8000/refresh_token' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTg5MzU3MzcsImlhdCI6MTYxODkzNTY3Nywic3ViIjoicm9oYW4ifQ.dja0E6SUaZfEvYVKySjLE9OLXOtob5pjpy3R_rlCD7c'

Response Body
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTg5MzU5MDcsImlhdCI6MTYxODkzNTg0Nywic3ViIjoicm9oYW4ifQ.VI1vqMZ2Mklue-bv5WtwhFxbVsbHkRHOr3fON49wpmE"
}

```