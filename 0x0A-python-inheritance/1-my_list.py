#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the builtin list class."""


    def print_sorted(self):
        """Printed a list in sorted ascending order."""
        print(sorted(self))
