from datetime import timezone, datetime, timedelta
from jose import jwt
from app.core.config import settings

def create_access_token(data: dict, expires_minutes: int = 1):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
