from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from app import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.User).offset(skip).limit(limit).all()


def create_user_c(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name = user.name, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_(db:Session, id:int, name : str):
    data = db.execute(update(models.User).where(models.User.id == id).values(name=name, hashed_password = name +"@1111"))
    db.commit()
    return data


def delete_user(db:Session, id:int):
    data = db.query(models.User).filter(models.User.id == id).first()
    if data:
        data = db.query(models.User).filter(models.User.id == id)
        data.delete()
        db.commit()
        return f"{id} deleted"
    else:
        return f"{id} does not exist"