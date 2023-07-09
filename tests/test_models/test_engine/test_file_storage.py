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
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()

        self.assertIn("BaseModel." + b.id, models.storage.all().keys())
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn("State." + s.id, models.storage.all().keys())
        self.assertIn("Place." + p.id, models.storage.all().keys())
        self.assertIn("City." + c.id, models.storage.all().keys())
        self.assertIn("Amenity." + a.id, models.storage.all().keys())
        self.assertIn("Review." + r.id, models.storage.all().keys())
        self.assertIn("Review." + r.id, models.storage.all().keys())

        with self.assertRaises(Exception):
            models.storage.new(None)
        with self.assertRaises(Exception):
            models.storage.new([])

    def test_save(self):
        a1 = Amenity()
        models.storage.save()
        self.assertEqual(os.path.exists("file.json"), True)
        with self.assertRaises(TypeError):
            models.storage.save(None)
        with self.assertRaises(TypeError):
            models.storage.save([])

    def test_reload(self):
        c1 = City()
        models.storage.save()
        self.assertEqual(os.path.exists("file.json"), True)
        os.remove("file.json")
        self.assertEqual(os.path.exists("file.json"), False)

        f1 = FileStorage()
        f1.reload()
        all_objs = f1.all()
        self.assertIn("City.{}".format(c1.id), all_objs)

    def test_pycodestyle_conformance(self):
        """Test for PEP8
        """
        stg = 'tests/test_models/test_engine/test_file_storage.py'
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([stg])
        self.assertEqual(result.total_errors, 0, "Found errors")
