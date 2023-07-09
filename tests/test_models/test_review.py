"""Unittest for the Review class that inherits from BaseModel
"""


import unittest
import datetime
import pycodestyle
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review


class TestReview(unittest.TestCase):
    """Testing for a Review class"""

    def test_init(self):
        """Test for the instantiation"""
        r1 = Review()
        self.assertEqual(r1.place_id, "")
        self.assertEqual(r1.user_id, "")
        self.assertEqual(r1.text, "")
        self.assertEqual(type(r1.id), str)
        self.assertEqual(type(r1.updated_at), datetime.datetime)
        self.assertEqual(type(r1.created_at), datetime.datetime)
        self.assertIsInstance(r1, BaseModel)

        f1 = FileStorage()
        # f1._FileStorage__objects -> Accessing a private attribute
        self.assertNotEqual(f1._FileStorage__objects, {})
        self.assertIsInstance(
            f1._FileStorage__objects[f"Review.{r1.id}"], Review)

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py',
                                    'tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
