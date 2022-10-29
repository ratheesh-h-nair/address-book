from datetime import datetime
from pydantic import BaseModel,EmailStr


class AddressListModel(BaseModel):
    coordinates:list
    distance:int
    
class CreateAddressModel(BaseModel):
    name:str
    email:str
    address : str
    phone : str
    coordinates : list