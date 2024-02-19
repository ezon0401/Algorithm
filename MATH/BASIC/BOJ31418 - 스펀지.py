'''
BOJ 31418 - Sponge (https://www.acmicpc.net/problem/31418)

There is a W X H size sponge.
At every second, a virus can stay in its cell or move to an adjacent cell (8 directions).
Given the initial locations of viruses, print the possible combination of all viruses after T seconds.
'''

import sys


# 1. TO GET THE INPUT

mod = 998244353
width, height, virus_count, time = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

ans = 1

for virus in range(virus_count):
    
    col, row = map(int, sys.stdin.readline().split())
    
    left_below = (max(1, col-time), max(1, row-time))
    left_above = (max(1, col-time), min(height, row+time))
    right_below = (min(width, col+time), max(1, row-time))
    right_above = (min(width, col+time), min(height, row+time))
    
    area = (right_below[0] + 1 - left_below[0]) * (left_above[1] + 1 - left_below[1])
    ans = ((ans % mod) * (area % mod)) % mod

print(ans)