'''
BOJ 11003 - Find the minimum (https://www.acmicpc.net/problem/11003)

Given an array A, find min(A[i-L+1:i+1]) for each i.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

num_count, length = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

local_min = deque([])

for index in range(num_count):
    
    while len(local_min) > 0 and local_min[0][1] <= index - length:
        local_min.popleft()
    
    while len(local_min) > 0 and local_min[-1][0] > arr[index]:
        local_min.pop()
    
    local_min.append((arr[index], index))
    
    print(local_min[0][0], end = ' ')