import pytest
from tests.seq import PRIMES, SQUARES
from tests.prime_factors import gpf

KNOWN_GPF = {
    2: 2,
    3: 3,
    4: 2,
    5: 5,
    12: 3,
    70151295: 2557,
}


@pytest.mark.parametrize("num,expected", KNOWN_GPF.items())
def test_manual(num: int, expected: int) -> None:
    """Test the greatest prime factor function."""
    assert gpf(num) == expected


@pytest.mark.parametrize("num", PRIMES)
def test_primes(num: int) -> None:
    """Test the greatest prime factor function on primes"""
    assert gpf(num) == num


def test_one() -> None:
    """Test the greatest prime factor function raises on 1."""
    with pytest.raises(ValueError):
        gpf(1)


def test_zero() -> None:
    """Test the greatest prime factor function raises on 0."""
    with pytest.raises(ValueError):
        gpf(0)


@pytest.mark.parametrize("num", SQUARES)
def test_square(num: int) -> None:
    """Test the greatest prime factor function is bounded above by the square root."""
    assert gpf(num) <= num**0.5
