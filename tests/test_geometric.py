"""Test the geometric squareness function logic.
"""
import numpy as np
import pytest
from squareness import geometric_squareness

from tests.seq import PRIMES, SQUARES

KNOWN_CASES = {
    8: 1 / 2,
    15: 3 / 5,
    99: 9 / 11,
    70151295: 7671 / 9145,
}


@pytest.mark.parametrize("prime", PRIMES)
def test_prime(prime: int) -> None:
    """Test that geometric squareness is correct for primes."""
    assert geometric_squareness(prime) == 1 / prime


def test_one() -> None:
    """Test that geometric squareness is correct for 1."""
    assert geometric_squareness(1) == 1


def test_zero() -> None:
    """Test that geometric squareness is undefined for 0."""
    with pytest.raises(ValueError):
        geometric_squareness(0)


@pytest.mark.parametrize("square", SQUARES)
def test_squares(square: int) -> None:
    """Test that geometric squareness is correct for squares."""
    assert geometric_squareness(square) == 1


@pytest.mark.parametrize("number,expected", KNOWN_CASES.items())
def test_manual(number: int, expected: float) -> None:
    """Test that geometric squareness is correct for some manually-calculated cases."""
    assert np.isclose(geometric_squareness(number), expected)
