#!/usr/bin/python3
"""Base Model class module"""

import uuid
from datetime import datetime

class BaseModel:
    """
    This is the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiation
        Args:
            *args (tuple): tuple
            **kwargs (dict): dictionary
            id (str): unique id for the BaseModel
            created_at (str): current datetime when the instance is created
            updated_at (str): cureent datetime when the instance is created
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at':
                    self.__dict__[k] = datetime.strptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(
                        v, '%Y-%m-%dT%H:%M:%S.%f')
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            # Adding the instance to the storage system
            storage.new(self)

    def __str__(self):
        """
        The class representation
        """
        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        Save method updates the public instance attribute - updated_at
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Creates a dictionary representation of the class attributes
        Return:
            a dictionary containing all keys/values of __dict__
        """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict

