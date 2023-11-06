'''
BOJ 30461 - Fishing (https://www.acmicpc.net/problem/30461)

There is a lake of N * M size.
If a bait is at (i, j), a fisherman can catch fish at (0, j) ~ (i, j).
Then the bait moves to (i-1, j-1) until it is outside a lake.
Answer the queries (a, b): How many fish does the fisherman catch when she throws bait at (a, b)?
'''

import sys


# 1. TO GET THE INPUT

row_count, col_count, query_count = map(int, sys.stdin.readline().split())

lake = []
for row_input in range(row_count):
    row = list(map(int, sys.stdin.readline().split()))
    lake.append(row)


# 2. TO SOLVE THE PROBLEM
# lake[row][col] stores the number of fish the fisherman catches when she throws bait at (row, col).

for col_num in range(col_count):
    for row_num in range(1, row_count):
        lake[row_num][col_num] += lake[row_num-1][col_num]
    
for col_num in range(1, col_count):
    for row_num in range(1, row_count):
        lake[row_num][col_num] += lake[row_num-1][col_num-1]

for query in range(query_count):
    row_num, col_num = map(int, sys.stdin.readline().split())
    print(lake[row_num-1][col_num-1])