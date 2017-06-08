#!/usr/bin/python3
from models.base_model import BaseModel
import datetime
import uuid
import json
from models import storage
"""module: class User"""


class User(BaseModel):
    '''class User'''

    def __init__(self, *args, **kwargs):
        '''method: init'''
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
            storage.new(self)
