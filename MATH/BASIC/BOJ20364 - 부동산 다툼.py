'''
BOJ 20364 - Estate Dispute (https://www.acmicpc.net/problem/20364)

There is a binary tree-shaped village. 
Each duck requests a land X. If a land among a path from vertex 1 to X is occupied, the duck cannot occupy the land X.
Determine whether a duck can occupy the requested land. 
'''

import sys


# 1. TO GET THE INPUT

node_count, query_count = map(int, sys.stdin.readline().split())


# 2. TO ANSWER THE QUERIES

visited = [0 for index in range(pow(2, 20) + 1)]

for query in range(query_count):
    
    num = int(sys.stdin.readline())
    
    num_copy = num
    occupied = 0
    while num_copy != 0:
        if visited[num_copy] == 1:
            occupied = num_copy
        num_copy //= 2
    
    visited[num] = 1
    
    print(occupied)