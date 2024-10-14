from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from database import init_db
from  app.crud import address_
from app.dependency import get_db

from app import crud, models, schemas
from fastapi import APIRouter, Depends, status


router = APIRouter()

@router.post("/address")
def create_address(user_id : int, address: schemas.Address, db : Session = Depends(get_db)):
    return address_.create_new_address(user_id=user_id, db=db, address=address)