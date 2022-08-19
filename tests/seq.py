"""Initial terms from useful sequences of numbers
"""
import sympy

PRIMES = sympy.primerange(2, 100)
SQUARES = [idx**2 for idx in range(2, 100)]
