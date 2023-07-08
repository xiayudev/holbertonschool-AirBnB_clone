"""Unittest for the User class that inherits from BaseModel
"""


import unittest
import datetime
import pycodestyle
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser(unittest.TestCase):
    """Testing for a User class"""

    def test_to_init(self):
        """Test for the instantiation"""
        u1 = User()
        self.assertEqual(u1.email, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.first_name, "")
        self.assertEqual(u1.last_name, "")
        self.assertEqual(type(u1.id), str)
        self.assertEqual(type(u1.updated_at), datetime.datetime)
        self.assertEqual(type(u1.created_at), datetime.datetime)
        self.assertIsInstance(u1, BaseModel)

        f1 = FileStorage()
        # f1._FileStorage__objects -> Accessing a private attribute
        self.assertNotEqual(f1._FileStorage__objects, {})
        self.assertIsInstance(
            f1._FileStorage__objects[f"User.{u1.id}"], User)

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py',
                                    'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")