#!/usr/bin/python3
"""Define an object attribute lookup funtion."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
