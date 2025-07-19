from fastapi import status ,HTTPException, Depends, APIRouter

from .. import models, schemas
from ..database import engine, get_db
from ..utils import hash_password
from sqlalchemy.orm import Session
from .. import oauth2


router = APIRouter()

@router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
async def create_post(payload: schemas.CreateUser, db: Session = Depends(get_db)):

    hashed_password = hash_password(payload.password)
    payload.password = hashed_password

    post_dict = payload.model_dump()
    new_user = models.User(**post_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{id}", response_model=schemas.UserResponse)
async def get_user(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    selected_user = db.query(models.User).filter(models.User.id == id).first()
    if(selected_user != None):
        return selected_user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found")