#!usr/bin/python3

"""
Defines unittest for TestFileStorageWithNewClasses
"""

import unittest
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    def test_serialization_deserialization(self):
        

        state = State()
        state.name = "California"
        city = City()
        city.state_id = state.id
        city.name = "San Francisco"
        amenity = Amenity()
        amenity.name = "Wi-Fi"
        place = Place()
        place.city_id = city.id
        place.user_id = "user123"
        place.name = "Cozy Apartment"
        review = Review()
        review.place_id = place.id
        review.user_id = "user456"
        review.text = "Great place to stay"

        storage.new(state)
        storage.new(city)
        storage.new(amenity)
        storage.new(place)
        storage.new(review)

        storage.save()
        storage.reload()

        retrieved_state = storage.get(State, state.id)
        retrieved_city = storage.get(City, city.id)
        retrieved_amenity = storage.get(Amenity, amenity.id)
        retrieved_place = storage.get(Place, place.id)
        retrieved_review = storage.get(Review, review.id)

        self.assertEqual(retrieved_state.name, "California")
        self.assertEqual(retrieved_city.state_id, state.id)
        self.assertEqual(retrieved_amenity.name, "Wi-Fi")
        self.assertEqual(retrieved_place.name, "Cozy Apartment")
        self.assertEqual(retrieved_review.text, "Great place to stay")

if __name__ == '__main__':
    unittest.main()
