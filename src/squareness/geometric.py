"""Functions relating to geometric squareness.
"""
from squareness import middling_divisors

def geometric_squareness(num: int) -> float:
    r"""Return the geometric squareness of a number.

    The _geometric squareness_ of a number $n\geq 1$ is defined as the ratio
    $$s_g(n)=\frac{\mathcal{M}(n)}{\mathcal{M}'(n)}.$$
    where $\mathcal{M}'(n)$ and $\mathcal{M}(n)$ are the middling divisors of $n$.
    Note $s_g(n)=1$ for a square number, and $s_g(p_n)\to 0$ for the primes $p_n$ as $n\to\infty$.
    These the the bounds, so $0 \lt s_g(n) \leq 1$.

    Args:
        num (int): The number to find the squareness of.

    Returns:
        float: The geometric squareness of the number.
    """
    if num < 1:
        raise ValueError("Geometric squareness is undefined for numbers less than 1")

    low_middling, high_middling = middling_divisors(num)
    return low_middling / high_middling
