""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Marion Queen Ramos
Date: 09.02.2024
"""

from library_item import LibraryItem
from genre import Genre

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled. When exceptions are 'caught', display the exception 
    # message to the console.


    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.

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
    # Use your own unique invalid values for the inputs to the class.

    try:
        # Attempting to create an instance with an invalid item_id (non-numeric).
        invalid_library_item = LibraryItem("ABC", "1984", "George Orwell", Genre.FICTION, "Yes")
    except Exception as e:
        print(f"An error occurred while creating the LibraryItem with invalid inputs: {e}")

if __name__ == "__main__":
    main()
