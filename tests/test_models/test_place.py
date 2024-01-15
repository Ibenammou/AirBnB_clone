import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
from time import sleep


class TestPlace(unittest.TestCase):
    """Unittesting Place class"""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_created_at_public(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_user_id_public(self):
        place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)

    def test_instan_with_kwargs(self):
        d_time = datetime.now()
        d_time_i = d_time.isoformat()
        place = Place(id="123", created_at=d_time_i, updated_at=d_time_i)
        self.assertEqual(place.id, "123")
        self.assertEqual(place.created_at, d_time)
        self.assertEqual(place.updated_at, d_time)

    def test_args_unused(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_str_repr(self):
        d_time = datetime.now()
        d_time_r = repr(d_time)
        place = Place()
        place.id = "8602393"
        place.created_at = place.updated_at = d_time
        place_str = place.__str__()
        self.assertIn("[Place] (8602393)", place_str)
        self.assertIn("'created_at': " + d_time_r, place_str)
        self.assertIn("'updated_at': " + d_time_r, place_str)

    def test_guest_public(self):
        place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_night_price_public(self):
        place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_public(self):
        place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_public(self):
        place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("logitude", place.__dict__)


class TestPlaceSave(unittest.TestCase):
    """Unittesting to save Place class"""

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

    def test_save_one(self):
        place = Place()
        sleep(0.05)
        f_updated_at = place.updated_at
        place.save()
        self.assertLess(f_updated_at, place.updated_at)

    def test_save_two(self):
        place = Place()
        place1 = Place()
        place.save()
        self.assertTrue(hasattr(place, 'updated_at'))
        up_place = place.updated_at
        place1.save()
        self.assertTrue(hasattr(place1, 'updated_at'))
        up_place1 = place1.updated_at
        self.assertNotEqual(up_place, up_place1)


if __name__ == '__main__':
    unittest.main()

