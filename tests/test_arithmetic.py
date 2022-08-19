"""Test the arithmetic squareness function logic.
"""
import numpy as np
import pytest
from squareness import arithmetic_squareness, middling_divisors

from tests.seq import PRIMES, SQUARES

KNOWN_CASES = KNOWN_CASES = {
    8: 5 / 7,
    15: 6 / 7,
    99: 48 / 49,
    70151295: 35074910 / 35075647,
}


@pytest.mark.parametrize("prime", PRIMES)
def test_prime(prime: int) -> None:
    """Test that arithmetic squareness is correct for primes."""
    assert arithmetic_squareness(prime) == 0
    assert middling_divisors(prime) == (1, prime)


def test_one() -> None:
    """Test that arithmetic squareness is undefined for 1."""
    with pytest.raises(ValueError):
        arithmetic_squareness(1)


def test_zero() -> None:
    """Test that arithmetic squareness is undefined for 0."""
    with pytest.raises(ValueError):
        arithmetic_squareness(0)


@pytest.mark.parametrize("square", SQUARES)
def test_squares(square: int) -> None:
    """Test that arithmetic squareness is correct for squares."""
    assert arithmetic_squareness(square) == 1


@pytest.mark.parametrize("number,expected", KNOWN_CASES.items())
def test_manual(number: int, expected: float) -> None:
    """Test that arithmetic squareness is correct for some manually-calculated cases."""
    assert np.isclose(arithmetic_squareness(number), expected)
