from sqlalchemy.orm import Session

from . import models


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
         # Update  fields as needed
        db_user.email = user.email
        db_user.username = user.username  # Update the username field
        db_user.hashed_password = user.password
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

def create_news(db: Session, news: schemas.ItemCreate):
    db_news = models.News(title=news.title, text=news.text, added_by='system', fake=False)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def get_news_item(db: Session, news_id: int):
    return db.query(models.News).filter(models.News.id == news_id).first()

def update_news(db: Session, news_id: int, news: schemas.ItemCreate):
    db_news = db.query(models.News).filter(models.News.id == news_id).first()
    if db_news:
         # Update other fields as needed
        db_news.title = news.title
        db_news.text = news.text
        db.commit()
        db.refresh(db_news)
        return db_news
    return None #no effect 

def delete_news(db: Session, news_id: int):
    db_news = db.query(models.News).filter(models.News.id == news_id).first()
    if db_news:
        db.delete(db_news)
        db.commit()
        return True
    return False
