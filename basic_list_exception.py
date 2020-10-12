# Program Name: basic_list_exception.py
# Program Author: Russell Holmes
# Date: 11/12/2020
import unittest
from unittest.mock import patch

# initializes a list of user input
def make_list():
    a = []
    for i in range(0, 3, 1):
        foo = get_input()
        if foo.isnumeric() != 1:
            raise ValueError
        else:
            if int(foo) < 1:
                raise ValueError
            elif int(foo) > 50:
                raise ValueError
            else:
                a.append(int(foo))
    return a


# returns specified input
def get_input():
    return input()


# tests the list
class TestList(unittest.TestCase):
    @patch('basic_list_exception.get_input', return_value='5')
    def test_make_list(self, input):
        self.assertEqual(make_list(), [5, 5, 5])

    @patch('basic_list_exception.get_input', return_value='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):                        # pass input
        with self.assertRaises(ValueError):                             # this is familiar
            make_list()                                                 # call the function!

    @patch('basic_list_exception.get_input', return_value='0')
    def test_make_list_below_range(self, input):
        with self.assertRaises(ValueError):
            make_list()

    @patch('basic_list_exception.get_input', return_value='51')
    def test_make_list_above_range(self, input):
        with self.assertRaises(ValueError):
            make_list()
