#!usr/bin/python3
"""Defines unittests for user class"""
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def test_user_inherits_from_base_model(self):
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.__class__.__name__, "User")

if __name__ == '__main__':
    unittest.main()
