"""Unittest for the File Storage class
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
        self.assertNotEqual(FileStorage._FileStorage__file_path, None)
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(type(models.storage), FileStorage)

    def test_all(self):
        """Test for the all method"""
        self.assertEqual(type(models.storage.all()), dict)

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

    def test_save(self):
        self.assertRaises(TypeError, models.storage.save, None)

    def test_reload(self):
        self.assertRaises(TypeError, models.storage.reload, None)

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

        OBJ = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + b.id, OBJ)
        self.assertIn("User." + u.id, OBJ)
        self.assertIn("State." + s.id, OBJ)
        self.assertIn("Place." + p.id, OBJ)
        self.assertIn("City." + c.id, OBJ)
        self.assertIn("Amenity." + a.id, OBJ)
        self.assertIn("Review." + r.id, OBJ)
