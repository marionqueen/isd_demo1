""""
Description: A class to manage User objects.
Author: Marion Queen Ramos
Date: 09.02.2024
"""
from borrower_status import BorrowerStatus
from email_validator import validate_email, EmailNotValidError

class LibraryUser:
    """
    Represents a library user.

    Attributes:
        user_id (int): Unique user ID.
        name (str): User's name.
        email (str): User's email address.
        borrower_status (BorrowerStatus): User's current status.
    """

    def __init__(self, user_id: int, name: str, email: str, borrower_status: BorrowerStatus):
        """
        Initialize the user with provided values.

        Args:
            user_id (int): Must be an integer > 99.
            name (str): Cannot be blank.
            email (str): Must be a valid email.
            borrower_status (BorrowerStatus): Must be a valid status.

        Raises:
            ValueError: If validations fail.
        """
        if not isinstance(user_id, int):
            raise ValueError("User Id must be numeric.")
        if user_id <= 99:
            raise ValueError("Invalid User Id.")
        if not name:
            raise ValueError("Name cannot be blank.")
        try:
            validate_email(email)
        except EmailNotValidError:
            raise ValueError("Invalid email address.")
        if not isinstance(borrower_status, BorrowerStatus):
            raise ValueError("Invalid Borrower Status.")

        self._user_id = user_id
        self._name = name
        self._email = email
        self._borrower_status = borrower_status

    @property
    def user_id(self) -> int:
        """Return user_id."""
        return self._user_id

    @property
    def name(self) -> str:
        """Return name."""
        return self._name

    @property
    def email(self) -> str:
        """Return email."""
        return self._email

    @property
    def borrower_status(self) -> BorrowerStatus:
        """Return borrower_status."""
        return self._borrower_status

    def borrow_item(self) -> str:
        """
        Check if user can borrow an item.

        Returns:
            str: Eligibility message.

        Raises:
            Exception: If user is DELINQUENT.
        """
        if self._borrower_status == BorrowerStatus.DELINQUENT:
            raise Exception(f"{self._name} cannot borrow an item due to their {self._borrower_status.name} status.")
        return f"{self._name} is eligible to borrow the item."

    def return_item(self) -> str:
        """
        Handle item return.

        Returns:
            str: Return status message.
        """
        if self._borrower_status == BorrowerStatus.DELINQUENT:
            self._borrower_status = BorrowerStatus.ACTIVE
            return f"Item successfully returned. {self._name}'s status now changed to: {self._borrower_status.name}."
        return "Item successfully returned."
