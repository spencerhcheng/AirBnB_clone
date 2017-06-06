#!/usr/bin/python3
import datetime
import uuid
import json
from models import storage

"""module: class BaseModel"""


class BaseModel:
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """init"""
        self.id = str(uuid.uuid1())
        self.created_at = datetime.datetime.now()

    def save(self):
        """public instance method: save"""
        self.updated_at = str(datetime.datetime.now())
        j = self.to_json()
        storage.new(j)
        storage.save()

    def to_json(self):
        """public instance method: to_json """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__)})
        self.created_at = str(self.created_at)
        return new_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, str(self.id), self.__dict__)
