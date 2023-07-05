#!/usr/bin/python3
"""Module to work with the BaseModel class
"""


import uuid
import json
from datetime import datetime
from models import storage


class BaseModel:
    """The base class for the airbnb project"""

    def __init__(self, *args, **kwargs):
        """Constructor of the BaseModel class

        Args:
            *args (tuple): tuple of arguments
            **kwargs (dict): dict of arguments

        """
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'updated_at' or k == 'created_at':
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return human readable string format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the attribute updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary of the instance"""
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
