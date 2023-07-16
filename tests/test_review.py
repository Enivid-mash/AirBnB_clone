#!/usr/bin/python3
"""Test cases for Review class"""
import unittest
from os import getenv
import os
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """Represents the test for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up test fixture for the test"""
        cls.review = Review()
        cls.review.place_id = "9820-dcbh"
        cls.review.user_id = "145-fgh-cde"
        cls.review.text = "Great place with many fun activities"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.review

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Tests the pycodestyle """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_Review(self):
        """Checks for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attribute_review(self):
        """checking if review has attributes"""
        self.assertTrue('place_id' in self.review.__dict__)
        self.assertTrue('id' in self.review.__dict__)
        self.assertTrue('updated_at' in self.review.__dict__)
        self.assertTrue('created_at' in self.review.__dict__)
        self.assertTrue('user_id' in self.review.__dict__)
        self.assertTrue('text' in self.review.__dict__)

    def test_is_subclass_Review(self):
        """tests if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """tests attribute type for review"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Review(self):
        """tests if the save works"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
