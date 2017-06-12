#!/usr/bin/python3
import unittest
"""test_file_storgae module"""


class TestFileStorage(unittest.TestCase):
    """Class: TestFileStorgae"""

    def setUp(self):
        """Setting up the instance"""
        self.filestorage = FileStorage()

    def testattr(self):
        """Testing the attributes of FileStorage"""
        self.assertTrue(hasattr(self.filestorage, "__file_path"))
        self.assertTrue(hasattr(self.filestorage, "__objects"))
        self.assertFalse(hasattr(self.filestorage, "random_attr"))
        self.assertEqual(self.filestorage.__class__.__name__, "FileStorage")

    def testmethod(self):
        """Testing the methods of FileStorage"""
        self.filestorage.all()
        self.filestorage.new()
        self.filestorage.save()
        self.filestorage.reload()

if __name__ == '__main__':
    unittest.main()
