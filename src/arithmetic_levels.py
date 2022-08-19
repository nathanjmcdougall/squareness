"""A script to manually interogate the basis for discrete levels in the arithmetic squareness curve.
"""
import numpy as np

from squareness import arithmetic_squareness

nums = list(range(2, 5_000))

def print_tier_nums(tier_level: int) -> None:
    for num in nums:
        squareness = arithmetic_squareness(num)
        if np.isclose(squareness,(tier_level-1)*(num/tier_level+1) / (num-1)):
            print(num, end=', ')
    print('...', end='\n')

if __name__ == "__main__":
    print('Which tier would you like to print?')
    tier = int(input())
    print_tier_nums(tier)