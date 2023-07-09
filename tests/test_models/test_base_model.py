"""Unittest for the Base Model class
"""


import io
import os
import unittest
import datetime
import pycodestyle
from unittest import mock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Testing for a Base Model class"""

    def test_to_init(self):
        """Test for the __init__ method"""
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertEqual(type(b1.id), str)
        self.assertEqual(type(b1_dict['created_at']), str)
        self.assertEqual(type(b1_dict['updated_at']), str)
        self.assertIn('__class__', b1_dict)
        self.assertEqual(datetime.datetime, type(b1.created_at))
        self.assertEqual(datetime.datetime, type(b1.updated_at))
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertEqual(type(b2.updated_at), datetime.datetime)
        self.assertEqual(type(b2.created_at), datetime.datetime)
        self.assertNotIn('__class__', b2.__dict__)

        f1 = FileStorage()
        # f1._FileStorage__objects -> Accessing a private attribute
        self.assertIsInstance(
            f1._FileStorage__objects[f"BaseModel.{b1.id}"], BaseModel)
        self.assertIsInstance(
            f1._FileStorage__objects[f"BaseModel.{b2.id}"], BaseModel)

    def test_str(self):
        """Test for the __str__ method"""
        b3 = BaseModel()
        rst = f"[BaseModel] ({b3.id}) {b3.__dict__}\n"
        with mock.patch("sys.stdout", new=io.StringIO()) as fake:
            print(b3)
        assert fake.getvalue() == rst

    def test_save(self):
        """Test for the save method"""
        b4 = BaseModel()
        b4_update = b4.updated_at
        b4.save()
        self.assertNotEqual(b4_update, b4.updated_at)
        self.assertTrue(os.path.exists('file.json'))

    def test_to_dict(self):
        """Test for the to_dict method"""
        b1 = BaseModel()
        dict_ = b1.to_dict()
        self.assertIn('__class__', dict_)
        self.assertEqual(type(dict_['created_at']), str)
        self.assertEqual(type(dict_['updated_at']), str)
        self.assertNotEqual(dict_, b1.__dict__)

    def test_pycodestyle_conformance(self):
        """Test for PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py',
                                    'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")


if __name__ == '__main__':
    unittest.main()
