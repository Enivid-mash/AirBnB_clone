#!/usr/bin/python3
"""Test for the console"""
from unittest.mock import patch
from io import StringIO
import unittest
import pep8
import json
import console
import os
from console import HBNBCommand
import tests
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Tests for the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.cons = HBNBCommand()

    @classmethod
    def teardown(cls):
        """This will tear down at the end of the test"""
        del cls.cons

    def tearDown(self):
        """teardowns the file.json file"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Pycodestyle for console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """Checking for docstrings"""
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)

    def test_emptyline(self):
        """tests case for empty-line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """tets case for the quit command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Tests case for create command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("create abcder")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("all User")
            self.assertEqual("[User]", f.getvalue()[:7])

    def test_show(self):
        """Tests case for show command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("show asdfsdrfs")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("show BaseModel cdgh-123")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test case for the destroy command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy BaseModel 987654")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test destroy command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("destroy BaseModel abcdefr345")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_all(self):
        """Test all command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """Test update command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("update BaseModel 121212")
            self.assertEqual("** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("all User")
            obj = f.getvalue()
        the_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("update User " + the_id)
            self.assertEqual("** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("update User " + the_id + " Name")
            self.assertEqual("** value missing **\n", f.getvalue())

    def test_all(self):
        """Test case for all command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("all allmodles")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_count(self):
        """Test case for the count command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("eftsrseeh.count()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cons.onecmd("State.count()")
            self.assertEqual("0\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()
