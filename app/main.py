from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users, auth, votes
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# the following line is used to create the database tables
# Uncomment the line below if you want to create tables automatically
# currently this job is done by alembic migrations
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://www.google.com",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}
