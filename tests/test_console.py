#!/usr/bin/python3

"""Defines a unittests for console.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestHBNBConsole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.mock_stdout = StringIO()

    def tearDown(self):
        self.mock_stdout.close()

    def test_create(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("create User")
        output = self.mock_stdout.getvalue()
        self.assertTrue("User" in output)

    def test_show(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("show User 1234-5678")
        output = self.mock_stdout.getvalue()
        self.assertTrue("User" in output)

    def test_destroy(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("destroy User 1234-5678")
        output = self.mock_stdout.getvalue()
        self.assertTrue("User" in output)

    def test_all(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("all User")
        output = self.mock_stdout.getvalue()
        self.assertTrue("User" in output)

    def test_count(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("count User")
        output = self.mock_stdout.getvalue()
        self.assertTrue("User" in output)

    def test_update(self):
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd("User.update(1234-5678, {'email': 'newemail@example.com'})")
        output = self.mock_stdout.getvalue()
        self.assertTrue("User" in output)

if __name__ == '__main__':
    unittest.main()
 
