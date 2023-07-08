"""Unittest for the City class that inherits from BaseModel
"""


import unittest
import datetime
import pycodestyle
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Testing for a City class"""

    def test_init(self):
        """Test for instantiation"""
        c1 = City()
        self.assertEqual(c1.name, "")
        self.assertEqual(c1.state_id, "")
        self.assertEqual(type(c1.id), str)
        self.assertEqual(type(c1.updated_at), datetime.datetime)
        self.assertEqual(type(c1.created_at), datetime.datetime)
        self.assertIsInstance(c1, BaseModel)

        f1 = FileStorage()
        # f1._FileStorage__objects -> Accessing a private attribute
        self.assertIsInstance(
            f1._FileStorage__objects[f"City.{c1.id}"], City)
        self.assertNotEqual(f1._FileStorage__objects, {})

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py',
                                    'tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
