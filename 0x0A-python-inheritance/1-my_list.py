#!/usr/bin/python3
"""
that contains MyList class
"""


class MyList(list):
    """the subclass of list"""
    def __init__(self):
        """the initializes the object"""
        super().__init__()

    def print_sorted(self):
        """the prints sorted list"""
        print(sorted(self))
