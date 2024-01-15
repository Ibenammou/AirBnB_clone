import unittest
import os
from models.amenity import Amenity
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_instan_with_kwargs(self):
        d_time = datetime.now()
        d_time_i = d_time.isoformat()
        a = Amenity(id="861", created_at=d_time_i, updated_at=d_time_i)
        self.assertEqual(a.id, "861")
        self.assertEqual(a.created_at, d_time)
        self.assertEqual(a.updated_at, d_time)

    def test_two_amenities(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_name_public(self):
        a = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", a.__dict__)

    def test_two_amenities_ids(self):
        a1 = Amenity()
        sleep(0.05)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_dict_types(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_dict_contains_keys(self):
        a = Amenity()
        self.assertIn("id", a.to_dict())
        self.assertIn("created_at", a.to_dict())
        self.assertIn("updated_at", a.to_dict())
        self.assertIn("__class__", a.to_dict())

    def test_to_dict_args(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.to_dict(None)

    def test_str_repr(self):
        d_time = datetime.now()
        d_time_r = repr(d_time)
        a = Amenity()
        a.id = "8602393"
        a.created_at = a.updated_at = d_time
        a_str = a.__str__()
        self.assertIn("[Amenity] (8602393)", a_str)
        self.assertIn("'id': '8602393'", a_str)
        self.assertIn("'created_at': " + d_time_r, a_str)
        self.assertIn("'updated_at': " + d_time_r, a_str)


class TestAmenitySaving(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmpo")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmpo", "file.json")
        except IOError:
            pass

    def test_two_type_saves(self):
        a = Amenity()
        sleep(0.05)
        f_updated_at = a.updated_at
        a.save()
        s_updated_at = a.updated_at
        self.assertLess(f_updated_at, a.updated_at)
        sleep(0.05)
        a.save()
        self.assertLess(s_updated_at, a.updated_at)

    def test_one_type_save(self):
        a = Amenity()
        sleep(0.05)
        f_updated_at = a.updated_at
        a.save()
        self.assertLess(f_updated_at, a.updated_at)

    def test_args_save(self):
        a = Amenity()
        with self.assertRaises(TypeError):
            a.save(None)

    def test_save_updated_file(self):
        a = Amenity()
        a.save()
        a_id = "Amenity." + a.id
        with open("file.json", "r") as f:
            self.assertIn(a_id, f.read())


if __name__ == "__main__":
    unittest.main()
