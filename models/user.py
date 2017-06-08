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
        super().__init__(self)
        if (kwargs.get('id') is not None):
            self.email = kwargs.get('email')
            self.password = kwargs.get('password')
            self.first_name = kwargs.get('first_name')
            self.last_name = kwargs.get('last_name')
        else:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
            storage.new(self)
