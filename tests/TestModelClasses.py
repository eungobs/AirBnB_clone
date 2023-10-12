#!usr/bin/python3

"""
Defines unittest for class TestStateModel
"""
import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestStateModel(unittest.TestCase):

    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'name'))

    def test_default_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

class TestCityModel(unittest.TestCase):

    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'name'))
        self.assertTrue(hasattr(city, 'state_id'))

    def test_default_attributes(self):
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

class TestAmenityModel(unittest.TestCase):

    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'name'))

    def test_default_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

class TestPlaceModel(unittest.TestCase):

    def test_inheritance(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_default_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

class TestReviewModel(unittest.TestCase):

    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_default_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()

