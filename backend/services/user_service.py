from typing import Dict

from models.auth import UserInDB

_fake_db: Dict[str, Dict] = {
    "eric": {
        "username": "eric",
        "full_name": "eric lin",
        "email": "eric1231.tw@gmail.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


def get_user(username: str) -> UserInDB | None:
    if username in _fake_db:
        return UserInDB(**_fake_db[username])
    return None
