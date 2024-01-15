import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """ Unittests for testing the City class """

    def test_id_public(self):
        self.assertEqual(str, type(City().id))

    def test_state_id_public(self):
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_update_at_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_public(self):
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_two_city_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_city_update_ats(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_repr(self):
        d_time = datetime.now()
        d_time_r = repr(d_time)
        city = City()
        city.id = "8602393"
        city.created_at = city.updated_at = d_time
        city_str = city.__str__()
        self.assertIn("[City] (8602393)", city_str)
        self.assertIn("'created_at': " + d_time_r, city_str)
        self.assertIn("'updated_at': " + d_time_r, city_str)

    def test_to_dict(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_dict_with_added_attr(self):
        city = City()
        city.mid_name = "Blessing"
        city.num = 86
        self.assertEqual("Blessing", city.mid_name)
        self.assertIn("num", city.to_dict())

    def test_to_dict_args(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


class TestCitySaving(unittest.TestCase):
    """ Unittests to save method of the City class """

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

    def test_two_saves(self):
        city = City()
        sleep(0.05)
        f_updated_at = city.updated_at
        city.save()
        s_updated_at = city.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.05)
        city.save()
        self.assertLess(s_updated_at, city.updated_at)

    def test_save_with_args(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_one_save(self):
        city = City()
        sleep(0.05)
        f_updated_at = city.updated_at
        city.save()
        self.assertLess(f_updated_at, city.updated_at)


if __name__ == "__main__":
    unittest.main()

