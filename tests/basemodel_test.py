#!/usr/bin/python3
import unittest

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.basemodel = BaseModel()

    def testattr(self):
        self.assertTrue(hasattr(self.basemodel, "created_at"))
