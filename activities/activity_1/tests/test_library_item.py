"""
Description: Unit tests for the Book class.
Author: Marion Queen Ramos
Date: 09.02.2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py
"""

import unittest
from library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):

    def test_init_valid_inputs_sets_attributes(self):
        # Check if everything is set right with valid inputs
        user_id = 100
        name = "John Doe"
        email = "john.doe@example.com"
        borrow_status = "ACTIVE"

        library_item = LibraryItem(user_id, name, email, borrow_status)

        self.assertEqual(library_item._LibraryItem__user_id, user_id)
        self.assertEqual(library_item._LibraryItem__name, name)
        self.assertEqual(library_item._LibraryItem__email, email)
        self.assertEqual(library_item._LibraryItem__borrow_status, borrow_status)

    def test_init_non_numeric_user_id_raises_exception(self):
        # Make sure it blows up when user_id isn't a number
        user_id = "ABC"
        name = "John Doe"
        email = "john.doe@example.com"
        borrow_status = "ACTIVE"

        with self.assertRaises(ValueError) as context:
            LibraryItem(user_id, name, email, borrow_status)
        self.assertIn("User ID must be numeric", str(context.exception))

    def test_init_user_id_less_than_100_raises_exception(self):
        # Make sure it blows up if user_id is less than 100
        user_id = 50
        name = "John Doe"
        email = "john.doe@example.com"
        borrow_status = "ACTIVE"

        with self.assertRaises(ValueError) as context:
            LibraryItem(user_id, name, email, borrow_status)
        self.assertIn("User ID must be 100 or greater", str(context.exception))

    def test_init_blank_name_raises_exception(self):
        # Make sure it blows up when name is blank
        user_id = 100
        name = ""
        email = "john.doe@example.com"
        borrow_status = "ACTIVE"

        with self.assertRaises(ValueError) as context:
            LibraryItem(user_id, name, email, borrow_status)
        self.assertIn("Name cannot be blank", str(context.exception))

    def test_init_invalid_email_raises_exception(self):
        # Make sure it blows up if the email is not valid
        user_id = 100
        name = "John Doe"
        email = "invalid-email"
        borrow_status = "ACTIVE"

        with self.assertRaises(ValueError) as context:
            LibraryItem(user_id, name, email, borrow_status)
        self.assertIn("Invalid email address", str(context.exception))

    def test_init_invalid_borrow_status_raises_exception(self):
        # Make sure it blows up if borrow_status isn't valid
        user_id = 100
        name = "John Doe"
        email = "john.doe@example.com"
        borrow_status = "INVALID_STATUS"

        with self.assertRaises(ValueError) as context:
            LibraryItem(user_id, name, email, borrow_status)
        self.assertIn("Invalid borrow status", str(context.exception))

    def test_user_id_returns_user_id_attribute(self):
        # Just check if user_id comes back correctly
        user_id = 100
        library_item = LibraryItem(user_id, "John Doe", "john.doe@example.com", "ACTIVE")

        self.assertEqual(library_item.user_id, user_id)

    def test_name_returns_name_attribute(self):
        # Just check if name comes back correctly
        name = "John Doe"
        library_item = LibraryItem(100, name, "john.doe@example.com", "ACTIVE")

        self.assertEqual(library_item.name, name)

    def test_email_returns_email_attribute(self):
        # Just check if email comes back correctly
        email = "john.doe@example.com"
        library_item = LibraryItem(100, "John Doe", email, "ACTIVE")

        self.assertEqual(library_item.email, email)

    def test_borrow_status_returns_borrow_status_attribute(self):
        # Just check if borrow_status comes back correctly
        borrow_status = "ACTIVE"
        library_item = LibraryItem(100, "John Doe", "john.doe@example.com", borrow_status)

        self.assertEqual(library_item.borrow_status, borrow_status)

    def test_borrow_item_delinquent_user_raises_exception(self):
        # Make sure it stops you from borrowing if you're delinquent
        library_item = LibraryItem(100, "John Doe", "john.doe@example.com", "DELINQUENT")

        with self.assertRaises(Exception) as context:
            library_item.borrow_item()
        self.assertIn("User is delinquent", str(context.exception))

    def test_borrow_item_non_delinquent_user_returns_message(self):
        # Check if you get the right message when borrowing is allowed
        library_item = LibraryItem(100, "John Doe", "john.doe@example.com", "ACTIVE")

        result = library_item.borrow_item()

        self.assertEqual(result, "Item borrowed successfully")

    def test_return_item_delinquent_user_modifies_status(self):
        # Make sure status changes from DELINQUENT to ACTIVE when returning
        library_item = LibraryItem(100, "John Doe", "john.doe@example.com", "DELINQUENT")

        library_item.return_item()

        self.assertEqual(library_item.borrow_status, "ACTIVE")

    def test_return_item_returns_message(self):
        # Check if you get the right message when returning an item
        library_item = LibraryItem(100, "John Doe", "john.doe@example.com", "ACTIVE")

        result = library_item.return_item()

        self.assertEqual(result, "Item returned successfully")

if __name__ == '__main__':
    unittest.main()
