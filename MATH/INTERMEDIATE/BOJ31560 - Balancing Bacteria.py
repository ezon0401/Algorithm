'''
BOJ 31560 - Balancing Bacteria (https://www.acmicpc.net/problem/31560)

There is an array A. You can do the following operation as much as you want. 

(1) Choose power level L and an index i.
(2) Choose whether to add L to or subtract L from A[i]. If you change the value of A[i] by L, A[i-1] will change by L-1, ..., and so on.

Print the minimum number of operations to make all elements of A 0.
'''

import sys


# 1. TO GET THE INPUT

grass_count = int(sys.stdin.readline())
patch = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = 0
offset = 0
bonus_offset = 0

for index in range(grass_count):
    
    offset += bonus_offset
    
    patch[index] += offset
    ans += abs(patch[index])
    
    offset += -patch[index]
    bonus_offset += -patch[index]

print(ans)