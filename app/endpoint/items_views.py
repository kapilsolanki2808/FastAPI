from fastapi import Depends, APIRouter
from app import crud, schemas
from sqlalchemy.orm import Session
from app.dependency import get_db

router = APIRouter()
                                                                                                                                                                        

# def create_items(items : schemas.Item, user_id : int, db:Session = Depends(get_db)):
#     return crud.items.create_user_item(db=db, item=items, user_id=user_id)

# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.items.get_items(db, skip=skip, limit=limit)
#     return items



@router.post("/create/item")
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.items.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.items.get_items(db, skip=skip, limit=limit)
    return items