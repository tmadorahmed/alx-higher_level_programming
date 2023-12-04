#!/usr/bin/python3
"""that is Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """that Add a new attribute to an object if possible.

    Args:
        obj (any): object to add an attribute to.
        att (str): name of the attribute to add to obj.
        value (any): value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
