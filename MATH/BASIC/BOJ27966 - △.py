'''
BOJ 27966 - △ (https://www.acmicpc.net/problem/27966)

Construct a tree so that ∑ dist(i, j) is a minimum for all vertex pair (i, j).
'''

import sys


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM

print(pow(node_count - 1, 2))

for node in range(2, node_count + 1):
    print(1, node)