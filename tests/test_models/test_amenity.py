"""Unittest for the Amenity class that inherits from BaseModel
"""


import unittest
import pycodestyle
import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Testing for a Amenity class"""

    def test_init(self):
        """Test for instantiation"""
        a1 = Amenity()
        self.assertEqual(a1.name, "")
        self.assertEqual(type(a1.id), str)
        self.assertEqual(type(a1.updated_at), datetime.datetime)
        self.assertEqual(type(a1.created_at), datetime.datetime)
        self.assertIsInstance(a1, BaseModel)

        f1 = FileStorage()
        # f1._FileStorage__objects -> Accessing a private attribute
        self.assertIsInstance(
            f1._FileStorage__objects[f"Amenity.{a1.id}"], Amenity)
        self.assertNotEqual(f1._FileStorage__objects, {})

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py',
                                    'tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
