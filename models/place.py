#!/usr/bin/python3
"""Place class Module"""

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from os import getenv
import models
import shlex

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship



place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Class Place"""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship('Review', cascade='all, delete, delete-orphan',
                               backref='place')

        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """ gets reviews.id """
            allv = models.storage.all()
            _list_rev = []
            _list_res = []

            for key in allv:
                _myreview = key.replace('.', ' ')
                _myreview = shlex.split(_myreview)
                if (_myreview[0] == 'Review'):
                    _list_rev.append(allv[key])

            for element in _list_rev:
                if (element.place_id == self.id):
                    _list_res.append(element)
            return (_list_res)

        @property
        def amenities(self):
            """ gets amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ link amenity ids to attrs """

            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
