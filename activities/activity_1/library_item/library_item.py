""""
Description: A class to manage LibraryItem objects.
Author: Marion Queen Ramos
Date: 09.02.2024
"""

from genre import Genre

class LibraryItem:
    def __init__(self, title: str, author: str, genre: Genre):
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
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def genre(self) -> Genre:
        return self._genre
