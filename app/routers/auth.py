from fastapi import status ,HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from .. import models, schemas
from ..database import get_db
from .. import oauth2
from ..utils import hash_password, verify_password
from sqlalchemy.orm import Session


router = APIRouter(tags=['Authentication'])

@router.post("/login_user", response_model=schemas.AccessToken)
async def get_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    selected_user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if(selected_user != None):
        verified = verify_password(user_credentials.password, selected_user.password)
        if not verified:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
        access_token = oauth2.create_access_token({"user_id": selected_user.id})
        return {"access_token": access_token, "token_type": "Bearer"}
        
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")