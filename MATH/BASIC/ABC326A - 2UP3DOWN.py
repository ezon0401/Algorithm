'''
ABC326A - 2UP3DOWN (https://atcoder.jp/contests/abc326/tasks/abc326_a)

Takahashi uses the stairs when moving up two floors or less or moving down three floors or less.
Determine whether Takahashi will use the stairs to move from floor X to floor Y.
'''

import sys

# 1. TO SOLVE THE PROBLEM

start_floor, end_floor = map(int, sys.stdin.readline().split())
if start_floor - 3 <= end_floor <= start_floor + 2:
    print("Yes")
else:
    print("No")