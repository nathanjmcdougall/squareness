"""Test the middling divisors logic.
"""
from typing import Tuple

import pytest
from tests.seq import PRIMES, SQUARES
import squareness


KNOWN_CASES = {
    8: (2, 4),
    12: (3, 4),
    15: (3, 5),
    24: (4, 6),
    99: (9, 11),
    70151295: (7671, 9145),
}


@pytest.mark.parametrize("prime", PRIMES)
def test_prime(prime: int) -> None:
    """Test that middling divisors are correct for primes."""
    assert squareness.middling_divisors(prime) == (1, prime)


def test_one() -> None:
    """Test that middling divisors are correct for 1."""
    assert squareness.middling_divisors(1) == (1, 1)


def test_zero() -> None:
    """Test that middling divisors are correct for 0."""
    with pytest.raises(ValueError):
        squareness.middling_divisors(0)


@pytest.mark.parametrize("square", SQUARES)
def test_squares(square: int) -> None:
    """Test that middling divisors are correct for squares."""
    middling = int(square**0.5)
    assert squareness.middling_divisors(square) == (middling, middling)


@pytest.mark.parametrize("number,expected", KNOWN_CASES.items())
def test_manual(number: int, expected: Tuple[int, int]) -> None:
    """Test that middling divisors are correct for a given number."""
    assert squareness.middling_divisors(number) == expected
