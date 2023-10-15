#!usr/bin/python3
"""Defines unittests for state class"""
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def test_state_inherits_from_base_model(self):
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")
        self.assertEqual(state.__class__.__name__, "State")

if __name__ == '__main__':
    unittest.main()
