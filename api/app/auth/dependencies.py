from sqlalchemy.orm import Session
from app.auth.models import Code
from fastapi import Depends, HTTPException, status
from app.database import get_sync_session
from datetime import datetime
from app.config import TZ


async def valid_invitation_code(code: str, db: Session = Depends(get_sync_session)):
    code = db.query(Code).filter(Code.code == code, Code.ends_at > int(datetime.now(tz=TZ).timestamp())).one_or_none()
    if code is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect or expired invitation code")
