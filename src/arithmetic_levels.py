"""A script to manually interogate the basis for discrete levels in the arithmetic squareness curve.
"""
from squareness import arithmetic_squareness

nums = list(range(2, 5_000))

# Determined visually
TIER0_CUTOFF = 0.2
TIER1_CUTOFF = 0.6

for num in nums:
    squareness = arithmetic_squareness(num)
    if TIER0_CUTOFF < squareness < TIER1_CUTOFF:
        print(num, end=', ')
print('', end='\n')
