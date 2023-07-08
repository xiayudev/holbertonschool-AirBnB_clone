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
        pass

    def test_reload(self):
        pass
