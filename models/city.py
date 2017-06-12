#!/usr/bin/python3
"""module: city"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """class: City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """init"""
        super().__init__(self, *args, **kwargs)
