#!/usr/bin/python3
"""tests for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """this test suite will test the FileStorage"""

    @classmethod
    def setUpClass(cls):
        """sets up the test"""
        cls.storage = FileStorage()

    def tearDown(self):
        """tear down"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """test when is created"""
        storage = FileStorage()