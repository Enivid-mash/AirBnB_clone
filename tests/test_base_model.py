#!/usr/bin/python3
"""This is a unit test for base model"""
from os import getenv
import os
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        """setting up class fixture for the test"""
        cls.base = BaseModel()
        cls.base.name = "Ann"
        cls.base.num = 22

    @classmethod
    def teardown(cls):
        """for tearing down the test at the end"""
        del cls.base

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """pep8 Testing"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """Checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """checking if BaseModel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is a type of BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_BaseModel(self):
        """test if the save works""" 
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """tests if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, "BaseModel")
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
