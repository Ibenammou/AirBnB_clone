#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
import models
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        elif type(cls) == str:
            return ({k: v for k, v in self.__objects.items()
                    if v.__class__.__name__ == cls})
        else:
            return ({k: v for k, v in self.__objects.items()
                    if v.__class__ == cls})
        # return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        # with open(FileStorage.__file_path, 'w') as f:
        temp = {}
        # temp.update(FileStorage.__objects)
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """ Calls reload() for deserializing the JSON file to obj"""
        self.reload()
