#!/usr/bin/python3
"""Test cases for City class"""
import unittest
from os import getenv
import os
from models.city import City
from models.base_model import BaseModel
import pep8


class TestCity(unittest.TestCase):
    """Represents the test for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixture for the test"""
        cls.city = City()
        cls.city.name = "Nairobi"
        cls.city.state_id = "145-fgh-cde"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests the pycodestyle """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """Checks for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """checking if city has attributes"""
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """tests if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """tests attribute type for City """
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(type(self.city.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_City(self):
        """tests if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
