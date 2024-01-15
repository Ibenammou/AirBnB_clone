#!/usr/bin/python3
"""
Unittest to test the User class
"""

import unittest
from time import sleep
import models
from models.user import User
import os
from datetime import datetime


class TestUser(unittest.TestCase):
    """Testing the User class"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_instance_stored_in_obj(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_public(self):
        self.assertEqual(str, type(User().id))

    def test_email(self):
        self.assertEqual(str, type(User.password))

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_attributes(self):
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_str_representation(self):
        user = User()
        n_date = datetime.now()
        n_date_r = repr(n_date)
        user.id = "8602393"
        user.created_at = user.updated_at = n_date
        user_str = user.__str__()
        self.assertIn("[User] (8602393)", user_str)
        self.assertIn("'id': '8602393'", user_str)
        self.assertIn("'created_at': " + n_date_r, user_str)
        self.assertIn("'updated_at': " + n_date_r, user_str)

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_created_at(self):
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)


class TestUser_save_method(unittest.TestCase):
    """Unittest for testing the saving of User class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
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

    def test_one_save(self):
        user = User()
        sleep(0.05)
        f_updated_at = user.updated_at
        user.save()
        self.assertLess(f_updated_at, user.updated_at)

    def test_save_args(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)


if __name__ == '__main__':
    unittest.main()
