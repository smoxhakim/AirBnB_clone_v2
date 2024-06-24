#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Review(BaseModel):
    """ Review classto store review information """
    
    __tablename__ = 'reviews'
    
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        text = Column(String(1024), nullabal=False)
        place_id = Column(String(60), ForeignKey(place.id), nullabal=False)
        user_id = Column(String(60), ForeignKey(users.id), nullabal=False)
    
    else:
        place_id = ""
        user_id = ""
        text = ""
