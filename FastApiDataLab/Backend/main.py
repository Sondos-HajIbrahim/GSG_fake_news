from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from sql_files import crud, models
from sql_files.databse import engine,get_db
from schemas import UserCreate
from services import UserService
from sqlalchemy import and_
from sql_files.models import User
app = FastAPI()
user_service=UserService()



@app.post("/signup", response_model=User)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already registered
    if db.query(User).filter(and_(User.email == user.email)).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create the user
    db_user = user_service.create_user(db, user)
    return db_user


@app.get("/")
def hello_world():
    return {"Hello": "World"}

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8000)