#!/usr/bin/python3
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    state_id = ""
    name = ""
    def __init__ (self, *args, **kwargs):
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
