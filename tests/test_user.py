#!/usr/bin/python3
"""Test cases for User class"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):
    """Represents the test for the User class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixture for the test"""
        cls.user = User()
        cls.user.first_name = "Njeri"
        cls.user.last_name = "Muchiri"
        cls.user.email = "njeri@yahoo.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_User(self):
        """Tests the pycodestyle """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_User(self):
        """Checks for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attribute_User(self):
        """checking if User has attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)

    def test_is_subclass_User(self):
        """tests if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """tests attribute type for user"""
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)

    def test_save_User(self):
        """tests if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
