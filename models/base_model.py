#!/usr/bin/python3
""" Base model class module """
import uuid
import models
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel:
    """A class that defines all other models
    """

    id = Column(String(60), unique=True,
                nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """ A base model new instance
        """
        if kwargs:
            for kw, _val in kwargs.items():
                if kw == 'created_at' or kw == 'updated_at':
                    _val = datetime.strptime(_val, "%Y-%m-%dT%H:%M:%S.%f")
                if kw != '__class__':
                    setattr(self, kw, _val)

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def to_dict(self):
        """dictionary format of the class instance
        """

        _dictlist = dict(self.__dict__)
        _dictlist['__class__'] = str(type(self).__name__)
        _dictlist['created_at'] = self.created_at.isoformat()
        _dictlist['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in _dictlist.keys():
            del _dictlist['_sa_instance_state']
        return _dictlist

    def __str__(self):
        """returns a string
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string represent
        """
        return self.__str__()

    def delete(self):
        """ delete instance
        """

        models.storage.delete(self)

    def save(self):
        """updates updated_at to current time
        """

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
