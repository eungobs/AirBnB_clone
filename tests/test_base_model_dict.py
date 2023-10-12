#!usr/bin/python3
"""
Defines unittest for class TestBaseModelRecreation
"""

import unittest
from models.base_model import BaseModel

class TestBaseModelRecreation(unittest.TestCase):

    def test_recreate_instance_from_dict(self):
        
        data = {
            '__class__': 'BaseModel',
            'id': '12345',
            'created_at': '2023-01-01T00:00:00.000000',
            'name': 'Test Model'
        }


        new_instance = BaseModel(**data)

        self.assertEqual(new_instance.__class__.__name__, 'BaseModel')
        self.assertEqual(new_instance.id, '12345')
        self.assertEqual(new_instance.name, 'Test Model')

        self.assertIsInstance(new_instance.created_at, datetime)

if __name__ == '__main__':
    unittest.main()
