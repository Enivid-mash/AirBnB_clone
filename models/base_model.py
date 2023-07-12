#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime


class BaseModel:
    """This is the base class that defines all common attributes
    and methids of all other classes that will inherit from it"""
<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        """This is the base model instance
        Args:
            args: This won't be used
            kwargs: arguments for the constructor of the BaseModel
=======
    def __init__(self):
        """This is the base model instance
>>>>>>> 506a3ebe9d4600c1eab62cee73478cb5d3bd3cd8
        Attributes:
            id: unique random id
            created_at: creation date
            updated_at: updated date"""
<<<<<<< HEAD
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S:%f")
=======
>>>>>>> 506a3ebe9d4600c1eab62cee73478cb5d3bd3cd8
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
