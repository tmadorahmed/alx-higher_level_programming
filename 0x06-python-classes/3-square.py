#!/usr/bin/python3

"""That Define a class Square."""


class Square:
    """that Represent a square."""

    def __init__(self, size=0):
        """that Initialize a new square.

        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """that Return the current area of the square."""
        return (self.__size * self.__size)
