#!/usr/bin/python3
import unittest
from models.user import User
"""module: user_test"""


class TestUser(unittest.TestCase):
    """Class: TestUser"""
    def setUp(self):
        """instance setup"""
        self.user = User()

    def testattr(self):
        """Testing the attributes of User"""
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertFalse(hasattr(self.user, "updated_at"))
        self.assertFalse(hasattr(self.user, "random_attr"))
        self.assertFalse(hasattr(self.user, "name"))
        self.user.name = "Betty"
        self.user.age = 89
        self.assertTrue(hasattr(self.user, "name"))
        self.assertTrue(hasattr(self.user, "age"))
        delattr(self.user, "name")
        self.assertFalse(hasattr(self.user, "name"))
        self.assertEqual(self.user.__class__.__name__, "User")

    def testmethod(self):
        """Testing the methods of User"""
        self.user.save()
        self.assertTrue(hasattr(self.user, "updated_at"))

    def teststr(self):
        """Testing the str format of User"""
        s = "[{}] ({}) {}".format(self.user.__class__.__name__,
                                  str(self.user.id),
                                  self.user.__dict__)
        self.assertEqual(print(s), print(self.user))

if __name__ == '__main__':
    unittest.main()
