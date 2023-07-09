#!/usr/bin/python3
"""Unittest for
the File Storage
class
"""

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

    def test_basic(self):
        # self.assertNotEqual(FileStorage._FileStorage__file_path, None)
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        """Test for the all method"""
        self.assertEqual(type(models.storage.all()), dict)

    def test_new(self):
        """Tests the function new"""
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

    def test_save_argument(self):
        """Tests the function save with an argument"""
        self.assertRaises(TypeError, models.storage.save, None)

    def test_save(self):
        """Tests the function save"""
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()

        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()

        with open("file.json", "r") as f:
            j_text = f.read()
            self.assertIn("BaseModel." + b.id, j_text)
            self.assertIn("User." + u.id, j_text)
            self.assertIn("State." + s.id, j_text)
            self.assertIn("Place." + p.id, j_text)
            self.assertIn("City." + c.id, j_text)
            self.assertIn("Amenity." + a.id, j_text)
            self.assertIn("Review." + r.id, j_text)

    def test_reload_argument(self):
        """Tests the function reload with an argument"""
        self.assertRaises(TypeError, models.storage.reload, None)

    def test_reload(self):
        """Tests the function reload"""
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()

        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        models.storage.reload()

        objc = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + b.id, objc)
        self.assertIn("User." + u.id, objc)
        self.assertIn("State." + s.id, objc)
        self.assertIn("Place." + p.id, objc)
        self.assertIn("City." + c.id, objc)
        self.assertIn("Amenity." + a.id, objc)
        self.assertIn("Review." + r.id, objc)


if __name__ == "__main__":
    unittest.main()
