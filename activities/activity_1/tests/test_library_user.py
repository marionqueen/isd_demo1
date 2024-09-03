"""
Description: Unit tests for the LibraryUser class.
Author: Marion Queen Ramos
Date: 09.02.2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_library_user.py
"""

import unittest
from library_user import LibraryUser
from borrower_status import BorrowerStatus



class TestLibraryUser(unittest.TestCase):

    def test_init_valid_inputs_sets_attributes(self):
        # Check if attributes are set correctly with valid inputs
        user_id = 100
        name = "John Doe"
        email = "john.doe@example.com"
        borrower_status = BorrowerStatus.ACTIVE

        user = LibraryUser(user_id, name, email, borrower_status)

        self.assertEqual(user._LibraryUser__user_id, user_id)
        self.assertEqual(user._LibraryUser__name, name)
        self.assertEqual(user._LibraryUser__email, email)
        self.assertEqual(user._LibraryUser__borrower_status, borrower_status)

    def test_init_non_numeric_user_id_raises_exception(self):
        # Check if it raises an exception when user_id isn't a number
        user_id = "ABC"
        name = "John Doe"
        email = "john.doe@example.com"
        borrower_status = BorrowerStatus.ACTIVE

        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertIn("User Id must be numeric", str(context.exception))

    def test_init_user_id_less_than_100_raises_exception(self):
        # Check if it raises an exception when user_id is less than 100
        user_id = 99
        name = "John Doe"
        email = "john.doe@example.com"
        borrower_status = BorrowerStatus.ACTIVE

        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertIn("Invalid User Id.", str(context.exception))

    def test_init_blank_name_raises_exception(self):
        # Check if it raises an exception when name is blank
        user_id = 100
        name = ""
        email = "john.doe@example.com"
        borrower_status = BorrowerStatus.ACTIVE

        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertIn("Name cannot be blank", str(context.exception))

    def test_init_invalid_email_raises_exception(self):
        # Check if it raises an exception when email is invalid
        user_id = 100
        name = "John Doe"
        email = "invalid-email"
        borrower_status = BorrowerStatus.ACTIVE

        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertIn("Invalid email address.", str(context.exception))

    def test_init_invalid_borrower_status_raises_exception(self):
        # Check if it raises an exception when borrower_status is invalid
        user_id = 100
        name = "John Doe"
        email = "john.doe@example.com"
        borrower_status = "NOT_A_STATUS"  # Invalid status

        with self.assertRaises(ValueError) as context:
            LibraryUser(user_id, name, email, borrower_status)
        self.assertIn("Invalid Borrower Status.", str(context.exception))

    def test_user_id_returns_user_id_attribute(self):
        # Check if user_id returns the correct value
        user_id = 100
        user = LibraryUser(user_id, "John Doe", "john.doe@example.com", BorrowerStatus.ACTIVE)

        self.assertEqual(user.user_id, user_id)

    def test_name_returns_name_attribute(self):
        # Check if name returns the correct value
        name = "John Doe"
        user = LibraryUser(100, name, "john.doe@example.com", BorrowerStatus.ACTIVE)

        self.assertEqual(user.name, name)

    def test_email_returns_email_attribute(self):
        # Check if email returns the correct value
        email = "john.doe@example.com"
        user = LibraryUser(100, "John Doe", email, BorrowerStatus.ACTIVE)

        self.assertEqual(user.email, email)

    def test_borrower_status_returns_borrower_status_attribute(self):
        # Check if borrower_status returns the correct value
        borrower_status = BorrowerStatus.ACTIVE
        user = LibraryUser(100, "John Doe", "john.doe@example.com", borrower_status)

        self.assertEqual(user.borrower_status, borrower_status)

    def test_borrow_item_delinquent_user_raises_exception(self):
        # Check if borrow_item raises an exception when user is DELINQUENT
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.DELINQUENT)

        with self.assertRaises(Exception) as context:
            user.borrow_item()
        self.assertIn("cannot borrow an item due to their DELINQUENT status.", str(context.exception))

    def test_borrow_item_non_delinquent_user_returns_message(self):
        # Check if borrow_item returns a message when user is not DELINQUENT
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.ACTIVE)

        result = user.borrow_item()

        self.assertEqual(result, "John Doe is eligible to borrow the item.")

    def test_return_item_delinquent_user_modifies_status(self):
        # Check if return_item modifies status when user was DELINQUENT
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.DELINQUENT)

        result = user.return_item()

        self.assertEqual(user.borrower_status, BorrowerStatus.ACTIVE)
        self.assertEqual(result, "Item successfully returned. John Doe's status now changed to: ACTIVE.")

    def test_return_item_returns_message(self):
        # Check if return_item returns a message indicating item was returned
        user = LibraryUser(100, "John Doe", "john.doe@example.com", BorrowerStatus.ACTIVE)

        result = user.return_item()

        self.assertEqual(result, "Item successfully returned.")

if __name__ == '__main__':
    unittest.main()

