#!/usr/bin/python3
import datetime
import uuid
import json
from models import storage
"""module: class BaseModel"""


class BaseModel:
    """class BaseModel"""
    dt_format = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """init"""
        if (kwargs.get('id') is not None):
            if 'created_at' in kwargs:
                try:
                    kwargs['created_at'] = datetime.datetime.strptime
                    (kwargs['created_at'], self.dt_format)
                except:
                    pass
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """public instance method: save"""
        """upate time and save object to json file"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_json(self):
        """public instance method: to_json """
        new_dict = self.__dict__.copy()
        new_dict.update({'created_at': self.created_at.strftime
                         (self.dt_format)})
        new_dict.update({'__class__': str(self.__class__.__name__)})
        if hasattr(self, 'updated_at'):
            new_dict.update({'updated_at': self.updated_at.strftime
                             (self.dt_format)})
        return new_dict

    def __str__(self):
        """str overwirte"""
        return "[{}] ({}) {}".format(self.__class__.__name__, str(self.id),
                                     self.__dict__)
