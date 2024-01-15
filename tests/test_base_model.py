#!/usr/bin/python3
"""
unittest to test the BaseModel function
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import time
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Class to test the BaseModel Function
    """

    def test_init_no_args(self):
        # Testing initialization with args
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_init_with_kwargs(self):
        """Testing instantiation with arguments"""
        day = datetime.now()
        day_str = day.isoformat()
        b1 = BaseModel(id="25487", created_at=day_str, updated_at=day_str)
        self.assertEqual(b1.created_at, day)
        self.assertEqual(b1.id, "25487")
        self.assertEqual(b1.updated_at, day)

    def test_two_models_with_unique_id(self):
        """Testing to see if the unique id works"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_the_id_datatype(self):
        """Testing the id datatype"""
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_the_date_and_time_datatype(self):
        """Testing the datetime datatype"""
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_two_models_different_created_at(self):
        """Testing the datetime values for created_at"""
        b1 = BaseModel()
        time.sleep(2.00)
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_two_models_different_created_at(self):
        """Testing the datetime values for updated_at"""
        b1 = BaseModel()
        time.sleep(2.00)
        b2 = BaseModel()
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_init_raises(self):
        """Testing the exception raises"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_save_updates(self):
        obj = BaseModel()
        obj.save()
        obj_id = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())

    def test_to_dict_result_output(self):
        """Testing the to_dict method's output"""
        day = datetime.now()
        b1 = BaseModel()
        b1.id = "437812"
        b1.created_at = b1.updated_at = day
        my_dict = {
            'id': '437812',
            '__class__': 'BaseModel',
            'created_at': day.isoformat(),
            'updated_at': day.isoformat()
        }
        self.assertDictEqual(b1.to_dict(), my_dict)


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

