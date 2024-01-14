#!/usr/bin/python3
"""
unittest to test the BaseModel function
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Class to test the BaseModel Function
    """

    def test_init_no_args(self):
        # Testing initialization with args
        self.assertEqual(BaseModel, type(BaseModel()))

    # ... (rest of your tests)

    def test_save_updates(self):
        obj = BaseModel()
        obj.save()
        obj_id = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


class TestBaseModelSaveMethod(unittest.TestCase):
    """Unittesting to check the save method"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_method(self):
        # Testing the saving method
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_args(self):
        # test save args
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.save(None)


if __name__ == '__main__':
    unittest.main()

