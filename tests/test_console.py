#!/usr/bin/python3

"""
Defines a unittest for consol.py.
"""
import unittest
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def test_quit(self):
        """Test that 'quit' command exits the program"""
        with unittest.mock.patch('sys.stdout', new_callable=StringIO):
            with unittest.mock.patch('sys.stdin', StringIO('quit\n')):
                console = HBNBCommand()
                self.assertTrue(console.onecmd('quit'))

    def test_EOF(self):
        """Test that 'EOF' command exits the program"""
        with unittest.mock.patch('sys.stdout', new_callable=StringIO):
            with unittest.mock.patch('sys.stdin', StringIO('EOF\n')):
                console = HBNBCommand()
                self.assertTrue(console.onecmd('EOF'))

if __name__ == '__main__':
    unittest.main() 
