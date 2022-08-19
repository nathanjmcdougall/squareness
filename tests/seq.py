"""Initial terms from useful sequences of numbers
"""
import sympy

PRIMES = list(sympy.primerange(100))
SQUARES = [idx**2 for idx in range(2, 100)]
