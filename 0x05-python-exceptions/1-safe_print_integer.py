#!/usr/bin/python3

def safe_print_integer(value):
    """that Print an integer with "{:d}".format().

    Args:
        value (int): that is The integer to print.

    Returns:
        False If a TypeError or ValueError occurs
        Otherwise True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
