from math import ceil, floor
from typing import Tuple

from sympy import divisors


def middling_divisors(num: int) -> Tuple[int, int]:
    """Gives the two middle divisors of a number.

    The divisors of a number $n$ come in pairs which multiply to $n$; in general if $a|n$ then $a$
    and $n/a$ are paired divisors. The pair whose values are closest together are called
    middling divisors.

    Args:
        num (int): The number to find the middling divisors of.

    Returns:
        Tuple[int, int]: The middling divisors of the number in ascending order.
    """
    if num < 1:
        raise ValueError("Number must be greater than 0")

    factors = divisors(num)
    middle = (len(factors) - 1) / 2
    middlings = (factors[floor(middle)], factors[ceil(middle)])

    return middlings
