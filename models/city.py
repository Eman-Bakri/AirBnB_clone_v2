#!/usr/bin/python3
"""City module class"""

from models.base_model import BaseModel, Base
from models.place import Place

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class with state id & name"""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', cascade='all, delete, delete-orphan',
                          backref='cities')
