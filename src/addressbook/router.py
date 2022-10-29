from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from public import *
from .schemas import *
from .models import *
from .utils import *

router = APIRouter(
    responses={404: make_response(False,Response.ITEM_NOT_FOUND,[])},
)


@router.post("/create", tags=["Address Book"])
async def create_address(req:CreateAddressModel,db: Session = Depends(get_db)):
    try:
        req_dict = req.dict()
        print(req_dict)
        db_user = AddressBook(name=req_dict.get('name'),email=req_dict.get('email'),address=req_dict.get('address'),
                              phone=req_dict.get('phone'),latitude = req_dict['coordinates'][0],longitude = req_dict['coordinates'][1])
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        resp = db_user
        return make_response(True,Response.ADDRESS_ADDED_SUCCESSFULLY,[])
    except Exception as e:
        print(str(e))
        return failed_response()

@router.post("/list", tags=["Address Book"])
async def list_address(req:AddressListModel,db: Session = Depends(get_db)):
    try:
       db_resp = db.query(AddressBook).filter(AddressBook.is_active == True).all()
       req_dict = req.dict()
       response = []
       resp_dict = [item.__dict__ for item in db_resp]
       for item in resp_dict:
           distance = check_spacial_distance(float(item['latitude']),float(item['longitude']),float(req_dict['coordinates'][0]),float(req_dict['coordinates'][1]))
           print("Name = {} and Phone = {} and Distance = {}".format(item['name'],item['phone'],distance))
           if(distance <= 100):
               response.append(item)
       return make_response(True,Response.ADDRESS_FETCHED_SUCCESSFULLY,response)
    except Exception as e:
        print(str(e))
        return failed_response()
        