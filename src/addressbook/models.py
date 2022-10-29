from ast import Str
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from public import Base,engine


class AddressBook(Base):
    __tablename__ = "address_book"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    address = Column(String)
    phone = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    is_active = Column(Boolean, default=True)
    
Base.metadata.create_all(engine)