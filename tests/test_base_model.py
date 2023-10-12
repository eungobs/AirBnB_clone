#!usr/bin/python3
"""
A class to define unitest
"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        model = BaseModel()
        string_representation = str(model)
        self.assertIn("BaseModel", string_representation)
        self.assertIn(model.id, string_representation)

    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIn("id", model_dict)
        self.assertEqual(model_dict["id"], model.id)
        self.assertIn("created_at", model_dict)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertIn("updated_at", model_dict)
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
