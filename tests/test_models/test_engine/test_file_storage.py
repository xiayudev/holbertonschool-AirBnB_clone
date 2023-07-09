#!/usr/bin/python3
"""Unittest for
the File Storage
class
"""


import os
import models
import unittest
from models.city import City
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """Testing for a File Storage class"""

    def test_init(self):
        """Test for the instantiation"""
        f1 = FileStorage()
        self.assertIsNotNone(f1._FileStorage__file_path)
        self.assertEqual(f1._FileStorage__file_path, "file.json")

    def test_all(self):
        """Test for the all method"""
        f1 = FileStorage()
        f1_objs = f1.all()
        self.assertEqual(type(f1_objs), dict)

    def test_new(self):
        """Test for the new method"""
        u = User()
        self.assertIn("User." + u.id, models.storage.all().keys())

    def test_save(self):
        """Test for the save method"""
        self.assertRaises(TypeError, models.storage.save, None)

    def test_reload(self):
        """Test for the reload method"""
        a1 = BaseModel()
        a1.save()
        self.assertEqual(os.path.exists("file.json"), True)
        os.remove("file.json")
        self.assertEqual(os.path.exists("file.json"), False)
        self.assertEqual(models.storage.reload(), None)
        models.storage._FileStorage__objects.clear()
        self.assertEqual(len(models.storage._FileStorage__objects), 0)
        models.storage.new(a1)
        self.assertEqual(len(models.storage._FileStorage__objects), 1)
        self.assertEqual(models.storage.all(), {f"BaseModel.{a1.id}": a1})
        self.assertEqual(os.path.exists("file.json"), False)
        a1.save()
        self.assertEqual(os.path.exists("file.json"), True)
        models.storage._FileStorage__objects.clear()
        self.assertEqual(len(models.storage._FileStorage__objects), 0)
        models.storage.reload()
        self.assertEqual(len(models.storage._FileStorage__objects), 1)
        models.storage.save()


if __name__ == '__main__':
    unittest.main()
