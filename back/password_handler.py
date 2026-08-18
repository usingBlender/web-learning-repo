import bcrypt
from main import SECRET_KEY  # pyright: ignore[reportImplicitRelativeImport]

def hash_password(password: str) -> str:
    """password hashing using bcrypt"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")  # pyright: ignore[reportOptionalMemberAccess]

def verify_password(plain_pwd:str, hashed_pwd:str) -> bool:
    """verify a password against its hash with bcrypt"""
    return bcrypt.checkpw(
            plain_pwd.encode("utf-8"),
            hashed_pwd.encode("utf-8")
            )
