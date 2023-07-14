#!/usr/bin/python3
"""This class defines review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This represents the review class that inherits from base model
    Attributes:
        place_id: the place's id
        user_id: the user's id
        text: text review
        """
    place_id = " "
    user_id = " "
    text = " "
