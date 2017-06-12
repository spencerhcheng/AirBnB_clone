#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
"""test_file_torage module """


class TestFileStorage(unittest.TestCase):
    """Class: TestFileStorage"""
    def setUp(self):
        """setup method for FileStorage test class"""
        self.filestorage = FileStorage()

    def test_attrs(self):
        """test for presence of attributes"""
        self.assertFalse(hasattr(self.filestorage, "random_attr"))

if "__main__" == __name__:
    unittest.main()
