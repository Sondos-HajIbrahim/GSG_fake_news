from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_files import crud, models, schemas
from sql_files.databse import engine,get_db
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/")
def hello_world():
    return {"Hello": "World"}
