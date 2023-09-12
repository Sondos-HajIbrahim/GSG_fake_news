from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from sql_files import  models
from sql_files.databse import engine,get_db
import schemas
from services import UserService
app = FastAPI()
user_service=UserService()



@app.post("/signup/", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(db, user)

@app.get("/")
def hello_world():
    return {"Hello": "World"}

if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8000)