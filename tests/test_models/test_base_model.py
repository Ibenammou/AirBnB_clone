#!/usr/bin/python3
"""
unittest to test the BaseModel function
"""

import unittest
import models
import os
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import uuid

=======
class TestBaseModel(unittest.TestCase):
    """
    Class to test the BaseModel Function
    """

    def test_init_no_args(self):
        # Testing initialization with args
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_public_id(self):
        # checks if id is public
        self.assertEqual(str, type(BaseModel().id))

    def test_public_created_at_datetime(self):
        # checks if created datetime is public
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        # checks if updated datetime is public
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unused_args(self):
        obj = BaseModel(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_init_with_kwargs(self):
        # Testing BaseModel initialization with kwargs
        data = {
                'id': str(uuid.uuid4()),
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat(),
                'name': 'TestingObj'
        }
        obj = BaseModel(**data)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertTrue(hasattr(obj, 'name'))
        self.assertEqual(obj.id, data['id'])
        self.assertEqual(obj.name, data['name'])
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_without_kwargs(self):
        # Testing initialization without kwargs
=======
	# Testing initialization without kwarg
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_inst_with_None_kwargs(self):
        # test none kwargs
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_two_unique_ids(self):
        # Tests if two ids are unique
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_to_dict_method(self):
        # Testing the __dict__ method

=======
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_dict_type(self):
        # test the type of to_dict
        obj = BaseModel()
        self.assertTrue(dict, type(obj.to_dict))

    def test_dict_correct(self):
        # test to check the correctness of the keys
        obj = BaseModel()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_dict_add_attributes(self):
        # test to check on additino of attributes to dict
        obj = BaseModel()
        obj.name = "ALXAfrica"
        self.assertIn("name", obj.to_dict())

    def test_dict_with_arg(self):
        # test to check args in to_dict
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.to_dict(None)

    def test_str_method(self):
        # Testing the __str__ method
        obj_dt = datetime.now()
        obj_dt_r = repr(obj_dt)

        obj = BaseModel()
        obj.id = "8602393"
        obj.created_at = obj.updated_at = obj_dt

        obj_str = str(obj)

        self.assertIn("[BaseModel] (8602393)", obj_str)
        self.assertIn("'id': '8602393'", obj_str)
        self.assertIn("'created_at': " + obj_dt_r, obj_str)
        self.assertIn("'updated_at': " + obj_dt_r, obj_str)


class TestBaseModel_save_method(unittest.TestCase):
    """ unittesting to check the save method """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.ison", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
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

    def test_save_updates(self):
        obj = BaseModel()
        obj.save()
        obj_id = "BaseModel." + obj.id
        with open("file.json", "r") as f:
            self.assertIn(obj_id, f.read())


if __name__ == '__main__':
    unittest.main()
=======

if __name__ == '__main__':
	unittest.main()
