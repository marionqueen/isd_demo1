""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Marion Queen Ramos
Date: 09.02.2024
"""

from library_item import LibraryItem
from genre import Genre
from library_user import LibraryUser
from borrower_status import BorrowerStatus

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled. When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    try:
        library_item = LibraryItem(101, "The Catcher in the Rye", "J.D. Salinger", Genre.FICTION, False)
    except Exception as e:
        print(f"An error occurred while creating the LibraryItem with valid inputs: {e}")

    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.

    try:
        print(f"Item ID: {library_item.item_id}")
    except Exception as e:
        print(f"An error occurred while accessing the item_id: {e}")

    try:
        print(f"Title: {library_item.title}")
    except Exception as e:
        print(f"An error occurred while accessing the title: {e}")

    try:
        print(f"Author: {library_item.author}")
    except Exception as e:
        print(f"An error occurred while accessing the author: {e}")

    try:
        print(f"Genre: {library_item.genre}")
    except Exception as e:
        print(f"An error occurred while accessing the genre: {e}")

    try:
        print(f"Is Borrowed: {library_item.is_borrowed}")
    except Exception as e:
        print(f"An error occurred while accessing the is_borrowed status: {e}")

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    try:
        # Attempting to create an instance with an invalid item_id (non-numeric).
        invalid_library_item = LibraryItem("ABC", "1984", "George Orwell", Genre.FICTION, "Yes")
    except Exception as e:
        print(f"An error occurred while creating the LibraryItem with invalid inputs: {e}")

    # --- New Code for LibraryUser Class ---

    # 4. Create an instance of the LibraryUser class with valid inputs.
    try:
        library_user = LibraryUser(202, "Jane Doe", "jane.doe@example.com", BorrowerStatus.ACTIVE)
    except Exception as e:
        print(f"An error occurred while creating the LibraryUser with valid inputs: {e}")

    # 5. Print each attribute of the LibraryUser instance using accessors.
    try:
        print(f"User ID: {library_user.user_id}")
    except Exception as e:
        print(f"An error occurred while accessing the user_id: {e}")

    try:
        print(f"Name: {library_user.name}")
    except Exception as e:
        print(f"An error occurred while accessing the name: {e}")

    try:
        print(f"Email: {library_user.email}")
    except Exception as e:
        print(f"An error occurred while accessing the email: {e}")

    try:
        print(f"Borrower Status: {library_user.borrower_status}")
    except Exception as e:
        print(f"An error occurred while accessing the borrower_status: {e}")

    # 6. Invoke the borrow_item method and print the result.
    try:
        borrow_result = library_user.borrow_item()
        print(borrow_result)
    except Exception as e:
        print(f"An error occurred while borrowing an item: {e}")

    # 7. Invoke the return_item method and print the result.
    try:
        return_result = library_user.return_item()
        print(return_result)
    except Exception as e:
        print(f"An error occurred while returning an item: {e}")

    # 8. Create an instance of the LibraryUser class with one or more invalid inputs.
    try:
        # Attempting to create an instance with an invalid email.
        invalid_library_user = LibraryUser(202, "Jane Doe", "invalid-email", BorrowerStatus.ACTIVE)
    except Exception as e:
        print(f"An error occurred while creating the LibraryUser with invalid inputs: {e}")

if __name__ == "__main__":
    main()
