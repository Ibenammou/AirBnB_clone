#!/usr/bin/python3
"""
Unittests for State class
"""

import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from models.state import State
import os


class TestState(unittest.TestCase):
    """ Unittests for testing the State class """
    def test_id_public(self):
        self.assertEqual(str, type(State().id))

    def test_datetime_public(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_public(self):
        state = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_unique(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_str_repr(self):
        d_time = datetime.now()
        d_time_r = repr(d_time)
        state = State()
        state.id = "8602393"
        state.created_at = state.updated_at = d_time
        state_str = state.__str__()
        self.assertIn("[State] (8602393)", state_str)
        self.assertIn("'id': '8602393'", state_str)
        self.assertIn("'created_at': " + d_time_r, state_str)
        self.assertIn("'updated_at': " + d_time_r, state_str)

    def test_unused_args(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instant_with_kwargs(self):
        d_time = datetime.now()
        d_time_i = d_time.isoformat()
        state = State(id="861", created_at=d_time_i, updated_at=d_time_i)
        self.assertEqual(state.id, "861")
        self.assertEqual(state.created_at, d_time)
        self.assertEqual(state.updated_at, d_time)

    def test_inst_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_saving(unittest.TestCase):
    """ 
    Unittests for testing the saving of the State class
    """
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmpo")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmpo", "file.json")
        except IOError:
            pass

    def test_state_one_save(self):
        state = State()
        sleep(0.05)
        f_updated_at = state.updated_at
        state.save()
        s_updated_at = state.updated_at
        self.assertLess(f_updated_at, state.updated_at)
        sleep(0.05)
        state.save()
        self.assertLess(s_updated_at, state.updated_at)

    def test_save_args(self):
        state = State()
        state.save()
        state_id = "State" + state.id
        with open("file.json", "r") as f:
            self.assertIn(state.id, f.read())


if __name__ == '__main__':
    unittest.main()
