"""Functions relating to arithmetic squareness.
"""
from squareness import middling_divisors


def arithmetic_squareness(num: int) -> float:
    r"""Return the arithmetic squareness of a number.

    The _arithmetic squareness_ of a number $n>1$ is defined as
    $$s_a(n)=1-\frac{\mathcal{M}'(n)-\mathcal{M}(n)}{n-1}$$
    where $\mathcal{M}'(n)$ and $\mathcal{M}(n)$ are the middling divisors of $n$.
    Note $s_a(n)=1$ for a square number, and $s(p)= 0$ for a prime $p$.
    These the the bounds, so $0\leq s(n)\leq 1$.

    Args:
        num (int): The number to find the squareness of.

    Returns:
        float: The arithmetic squareness of the number.
    """
    if num < 2:
        raise ValueError("Arithmetic squareness is undefined for numbers less than 2")

    low_middling, high_middling = middling_divisors(num)
    s_a = 1 - (high_middling - low_middling) / (num - 1)
    return s_a
