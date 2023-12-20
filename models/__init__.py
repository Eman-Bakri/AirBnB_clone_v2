#!/usr/bin/python3
"""Module to create FileStorage instance"""
from os import getenv

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
