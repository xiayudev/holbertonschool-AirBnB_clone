#!/usr/bin/python3
"""Unittest for
the File Storage
class
"""


import os
import pycodestyle
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City


class TestFileStorage(unittest.TestCase):
    """Testing for a File Storage class"""

    def test_init(self):
        f1 = FileStorage()
        self.assertIsNotNone(f1._FileStorage__file_path)
        self.assertEqual(f1._FileStorage__file_path, "file.json")

    def test_all(self):
        """Test for the all method"""
        f1 = FileStorage()
        f1_objs = f1.all()
        self.assertEqual(type(f1_objs), dict)

    def test_new(self):
        u = User()
        self.assertIn("User." + u.id, models.storage.all().keys())

    def test_save(self):
        a1 = City()
        a1.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_reload(self):
        a1 = City()
        models.storage.save()
        self.assertEqual(os.path.exists("file.json"), True)
        os.remove("file.json")
        self.assertEqual(os.path.exists("file.json"), False)

        f1 = FileStorage()
        f1.reload()
        all_objs = f1.all()
        all_objs.clear()
        models.storage.new(a1)
        self.assertEqual(all_objs, {f"City.{a1.id}": a1})

    def test_pycodestyle_conformance(self):
        """Test for PEP8
        """
        stg = 'tests/test_models/test_engine/test_file_storage.py'
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([stg])
        self.assertEqual(result.total_errors, 0, "Found errors")


if __name__ == '__main__':
    unittest.main()
