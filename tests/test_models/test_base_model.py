"""Unittest for the Base Model class
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing for a Base Model class"""

    def test_to_init(self):
        """Test for the __init__ method"""
        b1 = BaseModel()
        print(b1)
        self.assertEqual(b1.id, 'HOla')
