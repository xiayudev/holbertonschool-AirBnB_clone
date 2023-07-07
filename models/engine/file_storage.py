#!/usr/bin/python3
"""Module to work with FileStorage class
"""


import json
import os.path
from typing import List


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as fe:
            dict_ = {k: v.to_dict() for k, v in self.__objects.items()}
            fe.write(json.dumps(dict_))

    def reload(self):
        """deserializes the JSON file to __objects (only if
            the JSON file (__file_path) exists)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as fe:
                dict_ = json.loads(fe.read())
            for k in dict_.keys():
                value = dict_[k]
                self.__objects[k] = eval(value['__class__'])(**value)
        else:
            pass
