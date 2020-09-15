import requests
import bcrypt

BASE = "http://127.0.0.1:8080/"


# res = requests.post(
#     BASE + "user", data={"username": "gorkemsavran", "password": "gorkem1234"})

# print(res.json())

res = requests.get(
    BASE + "user", data={"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImdvcmtlbXNhdnJhbiIsIm5hbWUiOiJhZG1pbjEiLCJyYW5rIjoiRW5naW5lZXIiLCJleHAiOjE1OTk1NzEyNzl9.Bi6e2jB3jYTgycVcyUVG99fnZU0FcWKoK13Q6aImPpI"})

print(res.json())


# "username": "gorkemsavran", "password": "gorkem1234"

# passwd = "gorkem123"


# print(bcrypt.hashpw(passwd.encode("utf-8"), bcrypt.gensalt()).decode())
