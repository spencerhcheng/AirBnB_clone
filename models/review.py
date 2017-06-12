#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""module: review"""


class Review(BaseModel):
    """class: Review"""
    test = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(self, *args, **kwargs)
