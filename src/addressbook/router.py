from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from ...public import *
from .schemas import *
from .models import *
from .utils import *

router = APIRouter(
    responses={404: make_response(False,Response.ITEM_NOT_FOUND,[])},
)


@router.post("/create", tags=["Address Book"])
async def create_address(db:Session,req:CreateAddressModel):
    try:
        db_user = AddressBook(name=req.name,email=req.email,address=req.address,phone=req.phone,latitude = req.coordinates[0],longitude = req.coordinates[1])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        resp = db_user
        return make_response(True,Response.ADDRESS_ADDED_SUCCESSFULLY,resp)
    except Exception as e:
        print(str(e))
        return failed_response()

@router.get("/", tags=["Address Book"])
async def create_address(db:Session,req:AddressListModel):
    try:
       db_resp = db.query(AddressBook)
       return make_response(True,Response.ADDRESS_FETCHED_SUCCESSFULLY,db_resp)
    except Exception as e:
        print(str(e))
        return failed_response()
        