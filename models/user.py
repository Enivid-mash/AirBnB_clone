#!/usr/bin/python3
"""This defines the class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class for user
    Attributes:
        email: email address
        password: login password
        first_name: first name
        last_name: last name
        """
    email = " "
    password = " "
    first_name = " "
    last_name = " "
