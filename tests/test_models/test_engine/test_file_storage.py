#!/usr/bin/python3
"""Unittest for
the File Storage
class
"""

import console
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

    def setUp(self):
        """
        """
        self.l_tests = ['test_new', 'test_save', 'test_reload']
        if self._testMethodName in self.l_tests:
            self.b = BaseModel()
            self.u = User()
            self.s = State()
            self.p = Place()
            self.c = City()
            self.a = Amenity()
            self.r = Review()

    def tearDown(self):
        """
        """
        all_objs = models.storage.all()
        if self._testMethodName in self.l_tests:
            all_objs.pop('BaseModel.' + self.b.id)
            all_objs.pop('User.' + self.u.id)
            all_objs.pop('State.' + self.s.id)
            all_objs.pop('Place.' + self.p.id)
            all_objs.pop('City.' + self.c.id)
            all_objs.pop('Amenity.' + self.a.id)
            all_objs.pop('Review.' + self.r.id)
            models.storage.save()

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

        self.assertIn("BaseModel." + self.b.id, models.storage.all().keys())
        self.assertIn("User." + self.u.id, models.storage.all().keys())
        self.assertIn("State." + self.s.id, models.storage.all().keys())
        self.assertIn("Place." + self.p.id, models.storage.all().keys())
        self.assertIn("City." + self.c.id, models.storage.all().keys())
        self.assertIn("Amenity." + self.a.id, models.storage.all().keys())
        self.assertIn("Review." + self.r.id, models.storage.all().keys())

    def test_save_argument(self):
        """Tests the function save with an argument"""
        self.assertRaises(TypeError, models.storage.save, None)

    def test_save(self):
        """Tests the function save"""

        models.storage.new(self.b)
        models.storage.new(self.u)
        models.storage.new(self.s)
        models.storage.new(self.p)
        models.storage.new(self.c)
        models.storage.new(self.a)
        models.storage.new(self.r)
        models.storage.save()

        with open("file.json", "r") as f:
            j_text = f.read()
            self.assertIn("BaseModel." + self.b.id, j_text)
            self.assertIn("User." + self.u.id, j_text)
            self.assertIn("State." + self.s.id, j_text)
            self.assertIn("Place." + self.p.id, j_text)
            self.assertIn("City." + self.c.id, j_text)
            self.assertIn("Amenity." + self.a.id, j_text)
            self.assertIn("Review." + self.r.id, j_text)

    def test_reload_argument(self):
        """Tests the function reload with an argument"""
        self.assertRaises(TypeError, models.storage.reload, None)

    def test_reload(self):
        """Tests the function reload"""

        models.storage.new(self.b)
        models.storage.new(self.u)
        models.storage.new(self.s)
        models.storage.new(self.p)
        models.storage.new(self.c)
        models.storage.new(self.a)
        models.storage.new(self.r)
        models.storage.save()
        models.storage.reload()

        objc = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + self.b.id, objc)
        self.assertIn("User." + self.u.id, objc)
        self.assertIn("State." + self.s.id, objc)
        self.assertIn("Place." + self.p.id, objc)
        self.assertIn("City." + self.c.id, objc)
        self.assertIn("Amenity." + self.a.id, objc)
        self.assertIn("Review." + self.r.id, objc)


if __name__ == "__main__":
    unittest.main()
