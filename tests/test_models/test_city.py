#!/usr/bin/python3
"""Defines unittests for city class"""
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def test_city_inherits_from_base_model(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")
        self.assertEqual(city.__class__.__name__, "City")

if __name__ == '__main__':
    unittest.main()
