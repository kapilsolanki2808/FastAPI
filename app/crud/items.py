from sqlalchemy.orm import Session
import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_student(db:Session, student : schemas.StudentSer):
    stu_obj = models.Student(id = student.id, name=student.name)
    import pdb;pdb.set_trace()
    db.add(stu_obj)
    db.commit()
    db.refresh(stu_obj)
    return stu_obj

def get_students(db:Session):
    db_students =  db.query(models.Student).all()
    return db_students