'''
ABC332B - Online Shopping (https://atcoder.jp/contests/abc332/tasks/abc332_b)

Takahashi has a glass with a capacity of G and a mug with a capacity of M.
He will perform the following operation K times.

- If the glass is filled with water, discard all the water from the glass.
- Otherwise, if the mug is empty, fill the mug with water.
- Otherwise, transfer water from the mug to the glass until the mug is empty or the glass is filled.
'''

import sys


# 1. TO GET THE INPUT

op_count, glass_max, mug_max = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM 

mug_water = 0
glass_water = 0

for op in range(op_count):
    if glass_water == glass_max:
        glass_water = 0
    elif mug_water == 0:
        mug_water = mug_max
    else:
        if mug_water >= glass_max - glass_water:
            mug_water -= glass_max - glass_water
            glass_water = glass_max
        else:
            glass_water += mug_water
            mug_water = 0

print(glass_water, mug_water)