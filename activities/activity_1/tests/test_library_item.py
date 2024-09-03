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
from genre import Genre

class TestLibraryItem(unittest.TestCase):

    def test_init_valid_inputs_sets_attributes(self):
        # Check if everything is set right with valid inputs
        item_id = 101
        title = "1984"
        author = "George Orwell"
        genre = Genre.FICTION
        is_borrowed = False

        library_item = LibraryItem(item_id, title, author, genre, is_borrowed)

        self.assertEqual(library_item._LibraryItem__item_id, item_id)
        self.assertEqual(library_item._LibraryItem__title, title)
        self.assertEqual(library_item._LibraryItem__author, author)
        self.assertEqual(library_item._LibraryItem__genre, genre)
        self.assertEqual(library_item._LibraryItem__is_borrowed, is_borrowed)

    def test_init_non_numeric_item_id_raises_exception(self):
        # Make sure it blows up when item_id isn't a number
        item_id = "ABC"
        title = "1984"
        author = "George Orwell"
        genre = Genre.FICTION
        is_borrowed = False

        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertIn("Item Id must be numeric", str(context.exception))

    def test_init_non_boolean_is_borrowed_raises_exception(self):
        # Make sure it blows up when is_borrowed isn't a boolean
        item_id = 101
        title = "1984"
        author = "George Orwell"
        genre = Genre.FICTION
        is_borrowed = "Yes"  # Invalid type, should be a boolean

        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertIn("Is Borrowed must be a boolean value", str(context.exception))

    def test_init_blank_title_raises_exception(self):
        # Make sure it blows up when title is blank
        item_id = 101
        title = ""
        author = "George Orwell"
        genre = Genre.FICTION
        is_borrowed = False

        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertIn("Title cannot be blank", str(context.exception))

    def test_init_blank_author_raises_exception(self):
        # Make sure it blows up when author is blank
        item_id = 101
        title = "1984"
        author = ""
        genre = Genre.FICTION
        is_borrowed = False

        with self.assertRaises(ValueError) as context:
            LibraryItem(item_id, title, author, genre, is_borrowed)
        self.assertIn("Author cannot be blank", str(context.exception))

    def test_item_id_returns_item_id_attribute(self):
        # Just check if item_id comes back correctly
        item_id = 101
        library_item = LibraryItem(item_id, "1984", "George Orwell", Genre.FICTION, False)

        self.assertEqual(library_item.item_id, item_id)

    def test_title_returns_title_attribute(self):
        # Just check if title comes back correctly
        title = "1984"
        library_item = LibraryItem(101, title, "George Orwell", Genre.FICTION, False)

        self.assertEqual(library_item.title, title)

    def test_author_returns_author_attribute(self):
        # Just check if author comes back correctly
        author = "George Orwell"
        library_item = LibraryItem(101, "1984", author, Genre.FICTION, False)

        self.assertEqual(library_item.author, author)

    def test_genre_returns_genre_attribute(self):
        # Just check if genre comes back correctly
        genre = Genre.FICTION
        library_item = LibraryItem(101, "1984", "George Orwell", genre, False)

        self.assertEqual(library_item.genre, genre)

    def test_is_borrowed_returns_is_borrowed_attribute(self):
        # Just check if is_borrowed comes back correctly
        is_borrowed = False
        library_item = LibraryItem(101, "1984", "George Orwell", Genre.FICTION, is_borrowed)

        self.assertEqual(library_item.is_borrowed, is_borrowed)

if __name__ == '__main__':
    unittest.main()
