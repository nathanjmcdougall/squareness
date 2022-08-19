"""Functionality relating to prime factors.
"""
from sympy import primefactors


def gpf(num: int) -> int:
    """The greatest prime factor of a number greater than 1.

    Args:
        num (int): The number to find the greatest prime factor of.

    Returns:
        int: The greatest prime factor of the number.
    """
    if num < 2:
        raise ValueError("Number must be greater than 1.")

    return primefactors(num)[-1]
