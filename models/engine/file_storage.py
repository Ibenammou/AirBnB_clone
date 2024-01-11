#!/usr/bin/python3
"""A class FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A class that serializes instances to a JSON file
    and deserializes JSON file to instances"""
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        """Class constructor"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionaries object"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes object to json file"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf=8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to object if it exit"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf=8') as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_dict[key] = eval(class_name)(**value)
            FileStorage.__objects = obj_dict
        except FileNotFoundError:
            return
