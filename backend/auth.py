from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from models import User
import os

SECRET_KEY = os.getenv("SECRET_KEY", "babymomo-secret-change-me-in-production-2026")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 12  # 12 hours

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def verify_password(plain: str, hashed: str) -> bool:
    if plain is None or hashed is None:
        return False
    plain = str(plain).strip()
    try:
        return pwd_context.verify(plain, hashed)
    except Exception:
        try:
            import bcrypt as _bcrypt
            return _bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))
        except Exception:
            return False


def get_password_hash(password: str) -> str:
    password = str(password).strip()
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    if not username:
        return None
    username = username.strip()
    user = db.query(User).filter(User.username == username).first()
    if user:
        return user
    # 忽略大小寫再查一次
    return db.query(User).filter(User.username.ilike(username)).first()


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="無法驗證憑證，請重新登入",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_username(db, username)
    if user is None or not user.is_active:
        raise credentials_exception
    return user


def require_roles(*roles):
    async def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role not in roles and current_user.role not in ("superadmin", "company_admin"):
            raise HTTPException(status_code=403, detail="權限不足")
        return current_user
    return role_checker
