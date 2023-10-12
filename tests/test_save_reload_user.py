#!usr/bin/python3
"""
Defines unittest for class TestUserModel
"""

import unittest
from models.user import User

class TestUserModel(unittest.TestCase):

    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_default_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

if __name__ == '__main__':
    unittest.main()
