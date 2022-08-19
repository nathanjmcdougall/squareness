"""Initial terms from useful sequences of numbers
"""
import sympy

PRIMES = sympy.primerange(1, 100)
SQUARES = [idx**2 for idx in range(1, 100)]
