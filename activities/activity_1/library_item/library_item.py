""""
Description: A class to manage LibraryItem objects.
Author: Marion Queen Ramos
Date: 09.02.2024
"""

from genre import Genre

class LibraryItem:
    """
    Represents an item in the library (e.g., a book).

    Attributes:
        title (str): The title of the item.
        author (str): The author of the item.
        genre (Genre): The genre of the item.
    """

    def __init__(self, title: str, author: str, genre: Genre):
        """
        Initializes the library item.

        Args:
            title (str): The title of the library item. Must not be blank.
            author (str): The author of the library item. Must not be blank.
            genre (Genre): The Genre of the library item. Must be a valid Genre.

        Raises:
            ValueError: If title or author is blank, or if genre is invalid.
        """
        if not title:
            raise ValueError("Title cannot be blank.")
        if not author:
            raise ValueError("Author cannot be blank.")
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")
        
        self._title = title
        self._author = author
        self._genre = genre

    @property
    def title(self) -> str:
        """Returns the item's title."""
        return self._title

    @property
    def author(self) -> str:
        """Returns the item's author."""
        return self._author

    @property
    def genre(self) -> Genre:
        """Returns the item's genre."""
        return self._genre