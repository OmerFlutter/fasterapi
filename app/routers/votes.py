from fastapi import status ,HTTPException, Depends, APIRouter
from typing import List, Optional
from .. import oauth2

from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/vote',
    tags=["Votes"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_vote(payload: schemas.Vote, db: Session = Depends(get_db), current_user: schemas.UserResponse = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == payload.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {payload.post_id} not found")
    vote = db.query(models.Vote).filter(models.Vote.post_id == payload.post_id, models.Vote.user_id == current_user.id).first()
    if payload.dir == 1:
        if vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User {current_user.id} has already voted for post {payload.post_id}")
        new_vote = models.Vote(user_id=current_user.id, post_id=payload.post_id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added successfully"}
    else:
        if not vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Vote for post {payload.post_id} not found")
        db.delete(vote)
        db.commit()
        return {"message": "Vote removed successfully"}