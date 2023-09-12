from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from sql_files import  models
from sql_files.databse import engine,get_db
import schemas
from services import UserService,NewsService
from typing import List

app = FastAPI()
user_service=UserService()
news_service=NewsService()



@app.post("/signup/", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db, user)

@app.post("/login/",response_model=schemas.UserLoginResponse)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    if not user_service.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    # Create and return a token for authentication (you need to implement token creation)
    token = user_service.create_access_token(data={"sub": user.email})
    return {"access_token": token}

@app.get("/news/", response_model=List[schemas.News])
def get_news_list(skip: int = 0, limit: int = 10,type:str="all", db: Session = Depends(get_db)):
    news = news_service.get_news(db, skip=skip, limit=limit,type=type)
    return news



@app.get("/")
def hello_world():
    return {"Hello": "World"}

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8000)