#!/usr/bin/python3
"""This defines the place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the place class that inherits from the base model class
    Attributes:
        city_id: the city's id
        user_id: the user's id
        name: the name
        description: place description
        number_rooms: the total number of rooms
        number_bathrooms: the total number of bathrooms
        max_guest: allowed number of guests
        price_by_night: price
        latitude: the place's latitude
        longitude: the place's longitude
        amenity_ids: the id of amenity
    """
    city_id = " "
    user_id = " "
    name = " "
    description= " "
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtude = 0.0
    amenity_ids = " "
    