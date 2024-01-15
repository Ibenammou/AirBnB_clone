import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage class"""

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        # Test all storage
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict, {})

    def test_new(self):
        # Test for new User
        user = User()
        self.storage.new(user)
        obj_dict = self.storage.all()
        self.assertEqual(len(obj_dict), 1)
        self.assertIn(f"User.{user.id}", obj_dict)

    def test_save_reload(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        obj_dict = self.storage.all()
        self.assertEqual(len(obj_dict), 1)
        self.assertIn(f"User.{user.id}", obj_dict)

    def test_save_file_existence(self):
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_no_file(self):
        self.storage.save()
        self.storage.__objects = {}
        self.storage.reload()
        obj_dict = self.storage.all()
        self.assertDictEqual(obj_dict, {})


if __name__ == '__main__':
    unittest.main()
