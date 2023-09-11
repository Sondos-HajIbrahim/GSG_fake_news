from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schemas import UserCreate, User

class UserService:
    password_hash = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_user(self, db: Session, user: UserCreate):
        hashed_password = self.password_hash.hash(user.password)
        db_user = User(email=user.email, username=user.username, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


