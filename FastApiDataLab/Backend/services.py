from sqlalchemy.orm import Session
from sqlalchemy import desc
from schemas import UserCreate
from sql_files.models import User,News
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from constants import SECRET_KEY,ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM

class UserService:
    password_hash = CryptContext(schemes=["bcrypt"], deprecated="auto")


    def create_user(self, db: Session, user: UserCreate):
        hashed_password = self.password_hash.hash(user.password)
        db_user = User(email=user.email, username=user.username, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def verify_password(self,plain_password: str, hashed_password:str):
        return self.password_hash.verify(plain_password, hashed_password)

    def create_access_token(self,data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt



class NewsService:
    def get_news(self,db: Session, skip: int, limit:int,type:str):
        news = db.query(News)

        if type=="fake":
            news=news.filter(News.fake==True)
        elif type=="true":
            news=news.filter(News.fake==False)

        news=news.order_by(desc(News.id)).offset(skip).limit(limit).all()

        return news
