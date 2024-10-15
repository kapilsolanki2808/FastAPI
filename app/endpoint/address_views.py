from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
# from database import init_db
from  app.crud import address_
from app.dependency import get_db

from app import crud, models, schemas
from fastapi import APIRouter, Depends, status


router = APIRouter()

@router.post("/create/address")
def create_address(user_id : int, address: schemas.Address, db : Session = Depends(get_db)):
    return address_.create_new_address(user_id=user_id, db=db, address=address)


@router.get("/get/address")
def list_address(skip: int = 0, limit: int = 100, db : Session = Depends(get_db)):
    import pdb;pdb.set_trace()
    obj = db.query(models.Address).order_by(models.Address.id).offset(skip).limit(limit).all()
    # obj = db.query(models.Address).offset(skip).limit(limit).all()
    return obj

@router.get("/query/practice")
def get_address(db : Session = Depends(get_db), skip = 0, limit = 10):
    return address_.get_address_c(db=db)

@router.delete("/delete/address")
def del_address(id : int, db : Session = Depends(get_db)):
    return address_.delete_address(id=id, db=db)