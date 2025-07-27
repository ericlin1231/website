import requests

BASE_URL = "http://localhost:8000"
session = requests.Session()
resp = session.post(
    f"{BASE_URL}/token",
    data={"username": "eric", "password": "secret"},
)
resp.raise_for_status()
token_data = resp.json()
access_token = token_data["access_token"]
print("登入成功，收到 token:", access_token)

session.headers.update({"Authorization": f"Bearer {access_token}"})

resp = session.get(f"{BASE_URL}/users/me/")
resp.raise_for_status()
user = resp.json()
print("目前使用者資訊：", user)

resp = session.get(f"{BASE_URL}/users/me/items/")
resp.raise_for_status()
items = resp.json()
print("使用者的 items：", items)
