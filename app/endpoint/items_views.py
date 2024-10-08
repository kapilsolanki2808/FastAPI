from fastapi import Depends, APIRouter
import crud.items
import schemas, crud
from sqlalchemy.orm import Session
from dependency import get_db

router = APIRouter()
                                                                                                                                                                        

@router.post("/create/item")
def create_items(items : schemas.Item, user_id : int, db:Session = Depends(get_db)):
    return crud.items.create_user_item(db=db, item=items, user_id=user_id)

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.items.get_items(db, skip=skip, limit=limit)
    return items
