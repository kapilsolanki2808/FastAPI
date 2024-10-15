from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from database import init_db
from  app.crud.user import get_users, create_user_c, update_user_, delete_user
from app.dependency import get_db


# init_db()

# # Dependency

from app import crud, models, schemas
from fastapi import APIRouter, Depends, status

router = APIRouter()

import os
os.environ["PREFECT_API_SERVICES_FLOW_RUN_NOTIFICATIONS_ENABLED"] = "false"

@router.post("/create/user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    import pdb;pdb.set_trace()
    email=user.email
    db_user = db.query(models.User).filter(models.User.email == email).first()
    # import pdb;pdb.set_trace()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user_c(db=db, user=user)



@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


# @router.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @router.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)

@router.patch("/update/user")
def update_user(id : int, name : str, db : Session = Depends(get_db)):
    # pass
    return update_user_(db=db, id=id, name=name)


@router.delete("/delete/user")
def del_user(id:int, db:Session = Depends(get_db)):
    return delete_user(id = id, db=db)