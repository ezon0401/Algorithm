'''
BOJ 5200 - Sand Castle (https://www.acmicpc.net/problem/5200)

The goal is to construct cylindrical towers in a plain patch of sand with a rectangular moat around it.
However, to bring sand from elsewhere or remove sand from the patch is impossible.
How many centimeters will the base level change?
'''

import sys
from math import pi


# 1. TO SOLVE THE PROBLEM

# First, try to build towers with the sand from the moat.
# Then, it is easy to calculate how many centimeters the base level should change.

test_count = int(sys.stdin.readline())

for test_num in range(1, test_count + 1):
    
    patch_width, patch_height, moat_width, moat_depth, building_count = map(float, sys.stdin.readline().split())
    building_count = int(building_count)
    
    sand_amount = (patch_width * patch_height - (patch_width - moat_width * 2) * (patch_height - moat_width * 2)) * moat_depth
    sand_needed = 0
    
    for building_input in range(building_count):
        building_height, building_radius = map(float, sys.stdin.readline().split())
        sand_needed += building_radius * building_radius * pi * building_height
        
    print("Data Set {}:".format(test_num))
    print(format((sand_amount - sand_needed) / (patch_width * patch_height), ".2f"))