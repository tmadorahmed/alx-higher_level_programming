#!/usr/bin/python3
"""that is Defines a square-printing function."""


def print_square(size):
    """that is Print a square with the # character.

    Args:
        size (int): height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")