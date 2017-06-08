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
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """public instance method: save"""
        """upate time and save object to json file"""
        self.updated_at = str(datetime.datetime.now())
        storage.save()

    def to_json(self):
        """public instance method: to_json """
        """creates a copy of self.__dict__ and update with atribute __class__"""
        new_dict = self.__dict__.copy()
        new_dict.update({'created_at': str(self.created_at)})
        new_dict.update({'__class__': str(self.__class__.__name__)})
        return new_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, str(self.id), self.__dict__)
