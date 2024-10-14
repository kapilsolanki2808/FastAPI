from sqlalchemy.orm import Session
from app import models, schemas


def create_new_address(db: Session, address : schemas.Address, user_id : int):
    db_item = models.Address(**address.model_dump(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item