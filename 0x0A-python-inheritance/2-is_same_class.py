#!/usr/bin/python3
"""that is Defines a class-checking function."""


def is_same_class(obj, a_class):
    """that Check if an object is exactly an instance of a given class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
