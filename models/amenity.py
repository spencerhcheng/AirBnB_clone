#!/usr/bin/python3
from models.base_model import BaseModel
"""module: amenity"""


class Amenity(BaseModel):
    """class: Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        if (kwargs.get('id') is not None):
            self.__dict__ = kwargs
        else:
            super().__init__(self)
