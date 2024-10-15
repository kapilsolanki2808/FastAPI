from sqlalchemy.orm import Session
from app import models, schemas
from .user import get_user
from sqlalchemy import text , union_all, select, delete, union, update

def create_new_address(db: Session, address : schemas.Address, user_id : int):
    # user_ = db.query(models.User).filter(models.User.id == user_id).first()
    user_ = get_user(db=db, user_id=user_id)
    if user_:
        db_item = models.Address(**address.model_dump(), user_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return "user_id does not exist"

def get_address_c(db : Session, skip = 0, limit = 10):
    # stmt = db.query(models.User, models.Address).join(models.User.address).order_by(models.User.email, models.Address.email_address)
    # stmt = db.query(models.User, models.Address).join(models.Address.user).where(models.User.id > 2)
    # stmt = db.query(models.User, models.Address).join(models.Address, models.User.id == models.Address.user_id)

    subq = select(models.Address, models.User).where(models.Address.email_address == "string@gmail.com").subquery()
    stmt = select(models.User, models.Address).join(subq, models.User.id == subq.c.user_id)




    
    # stmt = db.query(models.User, models.Address).join(models.Address.user)
    l = []
    for row in db.execute(stmt):
        # import pdb;pdb.set_trace()
        l.append(f"{row.User.email} {row.Address.email_address}")
        


    # stu= text("SELECT * FROM address LIMIT 3")
    # # stu= text("SELECT * FROM address where Address.id > 5") 

    # stu = stu.columns(models.Student.id, models.Student.name)
    # stu = db.query(models.Student).from_statement(stu)
    # st = []
    # for user_obj in db.execute(stu).scalars():
    #     st.append(user_obj)

    # u = union(select(models.User).where(models.User.id > 2))
    # union_ = db.query(models.User).from_statement(u).all()
    ##u_all = union_all(select(models.User).where(models.User.id > 2))
    ##union_all_ = db.query(models.User).from_statement(u_all).all()
    return l #,{"union_" : union_}, {"union_all" : union_all_}#, {"students":st},  

def delete_address(db:Session, id : int):
    import pdb;pdb.set_trace()
    add_ = db.query(models.Address).filter(models.Address.id == id).first()
    if add_:
        add_ = db.query(models.Address).filter(models.Address.id == id)
        add_.delete()
        db.commit()
        return f"object number {id} of Address has been deleted"
    else:
        return f"object {id} in Address model does not exist!"
    

