#!/usr/bin/python3
"""Test cases for Place class"""
import unittest
from os import getenv
import os
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Represents the test for the Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixture for the test"""
        cls.plc = Place()
        cls.plc.name = 'Arusha'
        cls.plc.city_id = '1234-4567-abcd-efgh'
        cls.plc.user_id = '987-fghi-jkmn'
        cls.plc.description = "At the heart of the city!"
        cls.plc.number_rooms = 2000
        cls.plc.number_bathrooms = 4
        cls.plc.max_guest = 900
        cls.plc.price_by_night = 100
        cls.plc.latitude = 200.0
        cls.plc.longitude = 100.0
        cls.plc.amenity_ids = ["5678-hgytytfg"]

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.plc

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Place(self):
        """Tests the pycodestyle """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Place(self):
        """Checks for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_attribute_Place(self):
        """checking if Place has attributes"""
        self.assertTrue('created_at' in self.plc.__dict__)
        self.assertTrue('id' in self.plc.__dict__)
        self.assertTrue('updated_at' in self.plc.__dict__)
        self.assertTrue('name' in self.plc.__dict__)
        self.assertTrue('city_id' in self.plc.__dict__)
        self.assertTrue('user_id' in self.plc.__dict__)
        self.assertTrue('description' in self.plc.__dict__)
        self.assertTrue('number_rooms' in self.plc.__dict__)
        self.assertTrue('number_bathrooms' in self.plc.__dict__)
        self.assertTrue('max_guest' in self.plc.__dict__)
        self.assertTrue('price_by_night' in self.plc.__dict__)
        self.assertTrue('longitude' in self.plc.__dict__)
        self.assertTrue('latitude' in self.plc.__dict__)
        self.assertTrue('amenity_ids' in self.plc.__dict__)


    def test_is_subclass_Place(self):
        """tests if Place is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.plc.__class__, BaseModel), True)

    def test_attribute_types_Place(self):
        """tests attribute type for place"""
        self.assertEqual(type(self.plc.name), str)
        self.assertEqual(type(self.plc.user_id), str)
        self.assertEqual(type(self.plc.city_id), str)
        self.assertEqual(type(self.plc.description), str)
        self.assertEqual(type(self.plc.number_bathrooms), int)
        self.assertEqual(type(self.plc.number_rooms), int)
        self.assertEqual(type(self.plc.max_guest), int)
        self.assertEqual(type(self.plc.price_by_night), int)
        self.assertEqual(type(self.plc.latitude), float)
        self.assertEqual(type(self.plc.longitude), float)
        self.assertEqual(type(self.plc.amenity_ids), list)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Place(self):
        """tests if the save works"""
        self.plc.save()
        self.assertNotEqual(self.plc.created_at, self.plc.updated_at)

    def test_to_dict_Place(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.plc), True)


if __name__ == "__main__":
    unittest.main()
