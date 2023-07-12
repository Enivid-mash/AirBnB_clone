#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime


class BaseModel:
    """This is the base class that defines all common attributes
    and methids of all other classes that will inherit from it"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string
        Return:
            returns a string of class name, the id and dictionary
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """returns a string representation"""
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_to to current"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Creates a dictionary of the class
        Return:
            returns a dictionary of all the key values in __dict__"""
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
