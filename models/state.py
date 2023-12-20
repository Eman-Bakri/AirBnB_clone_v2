#!/usr/bin/python3
"""State Module class"""

from models.base_model import BaseModel, Base
import models
from models.city import City
import shlex

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """Class State"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        allv = models.storage.all()
        _list_citi = []
        _list_res = []

        for kwd in allv:
            city = kwd.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                _list_citi.append(allv[kwd])

        for element in _list_citi:
            if (element.state_id == self.id):
                _list_res.append(element)
        return (_list_res)
