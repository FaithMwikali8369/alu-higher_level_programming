#!/usr/bin/python3
"""Defines an integers addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    float arguments are typecasted to ints before addition is perfomed.
    second integer has a defualt value of 98 if value is not specified
    Raise:
    TypeError: if either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))