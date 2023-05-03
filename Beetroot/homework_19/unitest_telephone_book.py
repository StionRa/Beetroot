import unittest
import json
from io import StringIO
from unittest.mock import patch
from telephone_book import Phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook('test.json')
        self.entry = {
            'first_name': 'John',
            'last_name': 'Doe',
            'country': 'USA',
            'telephone': '5551234'
        }

    def tearDown(self):
        with open('test.json', 'w') as f:
            json.dump([], f)

    def test_add_entry(self):
        # Test valid input
        user_input = ['John', 'Doe', 'USA', '5551234']
        with patch('builtins.input', side_effect=user_input):
            self.phonebook.add_entry()

        # Check that the entry was added to the phonebook
        self.assertEqual(self.phonebook.telephone_book[0], self.entry)

    def test_add_entry_valid_input(self):
        # Test adding a valid entry
        user_input = ['John', 'Doe', 'USA', '5551234']
        with patch('builtins.input', side_effect=user_input):
            self.phonebook.add_entry()

        # Check that the entry was added to the phonebook
        expected_entry = {
            'first_name': 'John',
            'last_name': 'Doe',
            'country': 'USA',
            'telephone': '5551234'
        }
        self.assertEqual(self.phonebook.telephone_book[-1], expected_entry)

    def test_add_entry_invalid_input(self):
        # Test empty input
        user_input = ['', 'Doe', 'USA', '5551234', 'John', 'Doe', 'USA', '5551234']
        with patch('builtins.input', side_effect=user_input):
            self.phonebook.add_entry()

        expected_entry = {
            'first_name': 'Doe',
            'last_name': 'Usa',
            'country': 'John',
            'telephone': '5551234'
        }
        self.assertEqual(self.phonebook.telephone_book[-1], expected_entry)

    def test_add_entry_invalid_first_name(self):
        # Test adding an entry with an invalid first name
        user_input = ['', '123', 'John', 'doe', 'USA', '5551234']
        with patch('builtins.input', side_effect=user_input):
            self.phonebook.add_entry()
        expected_entry = {
            'first_name': 'John',
            'last_name': 'Doe',
            'country': 'USA',
            'telephone': '5551234'
        }
        self.assertEqual(self.phonebook.telephone_book[-1], expected_entry)

    def test_search_entry_name(self):
        # Add an entry to the phonebook
        self.phonebook.telephone_book.append(self.entry)

        # Test valid search
        user_input = 'John'
        with patch('builtins.input', return_value=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.phonebook.search_entry_name()

        expected_output = 'John Doe: USA - 5551234\n'
        self.assertEqual(fake_out.getvalue(), expected_output)

    def test_search_entry_name_not_found(self):
        # Add an entry to the phonebook
        self.phonebook.telephone_book.append(self.entry)

        # Test search for a name that is not in the phonebook
        user_input = 'Jane'
        with patch('builtins.input', return_value=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.phonebook.search_entry_name()

        expected_output = 'Jane not found in the telephone book.\n'
        self.assertEqual(fake_out.getvalue(), expected_output)

    def test_delete_entry(self):
        # Add an entry to the phonebook
        self.phonebook.telephone_book.append(self.entry)

        # Test valid deletion
        user_input = '5551234'
        with patch('builtins.input', return_value=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.phonebook.delete_entry()

        expected_output = 'John Doe has been deleted from the telephone book.\n'
        self.assertEqual(fake_out.getvalue(), expected_output)

        # Check that the entry was deleted from the phonebook
        self.assertEqual(self.phonebook.telephone_book, [])

    def test_delete_entry_not_found(self):
        # Add an entry to the phonebook
        self.phonebook.telephone_book.append(self.entry)

        # Test deletion of an entry that is not in the phonebook
        user_input = '5554321'
        with patch('builtins.input', return_value=user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                self.phonebook.delete_entry()

        expected_output = '5554321 not found in the telephone book.\n'
        self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
