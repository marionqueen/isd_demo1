""""
Description: A class to manage LibraryItem objects.
Author: Marion Queen Ramos
Date: 09.02.2024
"""

from genre import Genre

class LibraryItem:
    """
    Represents a library item (like a book).

    Attributes:
        item_id (int): Unique ID for the item.
        title (str): Title of the item.
        author (str): Author of the item.
        genre (Genre): Genre of the item.
        is_borrowed (bool): True if the item is borrowed, False if available.
    """

    def __init__(self, item_id: int, title: str, author: str, genre: Genre, is_borrowed: bool):
        """
        Initialize with given values.

        Args:
            item_id (int): Unique ID, must be an integer.
            title (str): Title of the item.
            author (str): Author of the item.
            genre (Genre): Genre of the item.
            is_borrowed (bool): Borrow status, must be a boolean.

        Raises:
            ValueError: If item_id is not an integer.
            ValueError: If is_borrowed is not a boolean.
        """
        if not isinstance(item_id, int):
            raise ValueError("Item Id must be numeric.")
        if not isinstance(is_borrowed, bool):
            raise ValueError("Is Borrowed must be a boolean value.")

        self._item_id = item_id
        self._title = title
        self._author = author
        self._genre = genre
        self._is_borrowed = is_borrowed

    @property
    def item_id(self) -> int:
        """Return item_id."""
        return self._item_id

    @property
    def title(self) -> str:
        """Return title."""
        return self._title

    @property
    def author(self) -> str:
        """Return author."""
        return self._author

    @property
    def genre(self) -> Genre:
        """Return genre."""
        return self._genre

    @property
    def is_borrowed(self) -> bool:
        """Return is_borrowed status."""
        return self._is_borrowed
