"""Unittest for the Place class
"""


import unittest
import datetime
import pycodestyle
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing for a Review class"""

    def test_init(self):
        """Test for the instantiation"""
        p1 = Place()
        self.assertEqual(p1.name, "")
        self.assertEqual(p1.city_id, "")
        self.assertEqual(p1.user_id, "")
        self.assertEqual(p1.description, "")
        self.assertEqual(p1.number_rooms, 0)
        self.assertEqual(p1.number_bathrooms, 0)
        self.assertEqual(p1.max_guest, 0)
        self.assertEqual(p1.price_by_night, 0)
        self.assertEqual(p1.latitude, 0)
        self.assertEqual(p1.longitude, 0)
        self.assertEqual(p1.amenity_ids, [])
        self.assertEqual(type(p1.id), str)
        self.assertEqual(type(p1.updated_at), datetime.datetime)
        self.assertEqual(type(p1.created_at), datetime.datetime)
        self.assertIsInstance(p1, BaseModel)

        f1 = FileStorage()
        # f1._FileStorage__objects -> Accessing a private attribute
        self.assertIsInstance(
            f1._FileStorage__objects[f"Place.{p1.id}"], Place)
        self.assertNotEqual(f1._FileStorage__objects, {})

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py',
                                    'tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
