#!/usr/bin/python3
""" Module to define db_strorage new class """

from os import getenv
from models.base_model import Base
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.city import City
from models.review import Review

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


class DBStorage:
    """ DBstorage module to create tables"""
    __engine = None
    __session = None

    def __init__(self):
        """Initiates models"""

        _newuser = getenv("HBNB_MYSQL_USER")
        _passwrd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(_newuser, _passwrd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in db"""
        _obj_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            _obj_query = self.__session.query(cls)

            for element in _obj_query:
                kwd = "{}.{}".format(type(element).__name__, element.id)
                _obj_dict[kwd] = element

        else:
            _list_class = [State, City, User, Place, Review, Amenity]
            for clause in _list_class:
                _obj_query = self.__session.query(clause)

                for element in _obj_query:
                    kwd = "{}.{}".format(type(element).__name__, element.id)
                    _obj_dict[kwd] = element
        return (_obj_dict)

    def new(self, obj):
        """a new element in the db"""
        self.__session.add(obj)

    def reload(self):
        """to reload"""

        Base.metadata.create_all(self.__engine)
        _makesess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(_makesess)
        self.__session = Session()

    def delete(self, obj=None):
        """delete from current db"""
        if obj:
            self.session.delete(obj)

    def save(self):
        """save changes to current db"""
        self.__session.commit()

    def close(self):
        """ call to close()"""

        self.__session.close()

