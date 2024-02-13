'''
BOJ 15678 - Yonsei Water Park (https://www.acmicpc.net/problem/15678)

There is an array A. Joon-ho can start from any element. 
He can move to any element that is not farther than D indefinitely.
However, he can access each element only once.
Determine the maximum value of the sum of elements that Joon-ho accessed. 
'''

import sys


# 3. FUNCTIONS TO MANAGE THE SEGMENT TREE

def seg_add(index, val):
    
    index += align
    seg_tree[index] = val
    index >>= 1
    
    while index != 0:
        seg_tree[index] = max(seg_tree[index << 1], seg_tree[(index << 1) | 1])
        index >>= 1

def seg_delete(index):
    
    index += align
    seg_tree[index] = -inf
    index >>= 1
    
    while index != 0:
        seg_tree[index] = max(seg_tree[index << 1], seg_tree[(index << 1) | 1])
        index >>= 1


# 1. TO GET THE INPUT

arr_length, max_interval = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO CONSTRUCT A SEGMENT TREE
# The segment tree stores max(dp[N-1], ..., dp[N-D]).

inf = float('inf')

align = 1 << 17
seg_tree = [-inf for index in range(1 << 18)]


# 4. TO SOLVE THE PROBLEM (DP)

dp = [0 for index in range(arr_length)]

for index in range(arr_length):
    
    dp[index] = max(0, seg_tree[1]) + arr[index]
    seg_add(index, dp[index])
    if index >= max_interval:
        seg_delete(index - max_interval)

print(max(dp))