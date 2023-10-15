#!/usr/bin/python3
"""Defins unittests for amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def test_amenity_inherits_from_base_model(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")
        self.assertEqual(amenity.__class__.__name__, "Amenity")

if __name__ == '__main__':
    unittest.main()
