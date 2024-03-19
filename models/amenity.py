#!/usr/bin/python3
"""project """
import os
from sqlalchemy import  String , Column
from sqlalchemy.orm import relationship

from models.base_model import  Base , BaseModel


class Amenity(BaseModel, Base):
    """Amenity data """
    __tablename__ = 'amenities'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
