#!/usr/bin/python3
"""Defines unittests for review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def test_review_inherits_from_base_model(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertEqual(review.__class__.__name__, "Review")

if __name__ == '__main__':
    unittest.main()
