"""Unittest for the State class that inherits from BaseModel
"""


import unittest
import datetime
import pycodestyle
from unittest import mock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    """Testing for a State class"""

    def test_to_init(self):
        """Test for the instantiation"""
        s1 = State()
        self.assertEqual(s1.name, "")
        self.assertEqual(type(s1.id), str)
        self.assertEqual(type(s1.updated_at), datetime.datetime)
        self.assertEqual(type(s1.created_at), datetime.datetime)
        self.assertIsInstance(s1, BaseModel)

        f1 = FileStorage()
        # f1._FileStorage__objects -> Accessing a private attribute
        self.assertNotEqual(f1._FileStorage__objects, {})
        self.assertIsInstance(
            f1._FileStorage__objects[f"State.{s1.id}"], State)

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py',
                                    'tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
