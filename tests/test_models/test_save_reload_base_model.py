#!usr/bin/python3
"""
Defines unittest
"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageSerialization(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.bm = BaseModel()
        self.bm.id = "test_id"
        self.bm.name = "Test Model"
        self.bm.save()

    def test_serialization_and_deserialization(self):
        self.assertIn("BaseModel.test_id", self.storage.all())

        
        self.storage.save()

        self.assertTrue(os.path.exists("file.json"))

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn("BaseModel.test_id", new_storage.all())
        new_bm = new_storage.all()["BaseModel.test_id"]
        self.assertEqual(new_bm.id, "test_id")
        self.assertEqual(new_bm.name, "Test Model")

    def tearDown(self):

        if os.path.exists("file.json"):
            os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
