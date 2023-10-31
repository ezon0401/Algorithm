'''
BOJ 15724 - (https://www.acmicpc.net/problem/15724)

There is an N * M number grid and queries. 
A query consists of 4 numbers: x1, y1, x2, y2. 
It asks the sum of numbers covered by a rectangle of which the left-top vertex is (x1, y1) and the right-bottom vertex is (x2, y2).
Answer the queries.
'''

import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = [[0 for col_index in range(col_count + 1)]]
for row_input in range(row_count):
    row = [0] + list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 2. TO STORE PREFIX SUM
# grid[i][j] stores the sum of numbers covered by a rectangle of which two vertices are (0, 0) and (i, j).

for row_index in range(1, row_count + 1):
    for col_index in range(1, col_count + 1):
        grid[row_index][col_index] += grid[row_index-1][col_index] + grid[row_index][col_index-1] - grid[row_index-1][col_index-1]


# 3. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())
for query_input in range(query_count):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(grid[x2][y2] - grid[x2][y1-1] - grid[x1-1][y2] + grid[x1-1][y1-1])