#!/usr/bin/python3
"""Module to work with the BaseModel class
"""


import uuid
from datetime import datetime


class BaseModel:
    """The base class for the airbnb project"""

    def __init__(self):
        """Constructor of the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return human readable string format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary of the instance"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
