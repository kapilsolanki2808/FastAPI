from fastapi import Depends, FastAPI, HTTPException
from .dependency import get_db
from .database import SessionLocal, engine, init_db
from  .endpoint import address_views, users_views, items_views
init_db()

app = FastAPI()

app.include_router(users_views.router, prefix="/users_views", tags=["users_views"])
app.include_router(items_views.router, prefix="/items_view",tags=["item_users"])
app.include_router(address_views.router, prefix="/address_view",tags=["address_users"])

