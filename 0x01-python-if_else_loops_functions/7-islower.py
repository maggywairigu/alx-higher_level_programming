#!/usr/bin/python
#7-islower.py

def islower(c):
    ""Checks for lowercase characters.""
    if ord(c) >= 97 ord(c) <= 122:
        return True
    else:
        return False
