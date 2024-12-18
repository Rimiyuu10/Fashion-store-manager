import hashlib


def hash_password(password: str | None) -> str | None:
    if password is None:
        return None
    return hashlib.md5(password.encode()).hexdigest()