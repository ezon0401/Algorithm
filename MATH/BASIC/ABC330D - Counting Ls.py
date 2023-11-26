'''
ABC330D - Counting Ls (https://atcoder.jp/contests/abc330/tasks/abc330_d)

You are given an N * N grid consisting of 'o' and 'x'.
Find the number of triples of cells that satisfy all of the following conditions.

(1) Three cells are distinct.
(2) Three cells have an 'o' written in them.
(3) Exactly two of the cells are in the same row.
(4) Exactly two of the cells are in the same column.
'''

import sys


# 1. TO GET INPUT
# row_o and col_o count number of 'o's in each row and column.

grid_size = int(sys.stdin.readline())

row_o = [0 for row_num in range(grid_size)]
col_o = [0 for col_num in range(grid_size)]

grid = []
for row_num in range(grid_size):
    row = list(sys.stdin.readline().strip())
    grid.append(row)
    for col_num in range(grid_size):
        if row[col_num] == "o":
            row_o[row_num] += 1
            col_o[col_num] += 1


# 2. TO SOLVE THE PROBLEM
# Three cells in a triple must be (row_num, col_num), (row_num, Y), and (X, col_num).

ans = 0
for row_num in range(grid_size):
    for col_num in range(grid_size):
        if grid[row_num][col_num] == "o":
            ans += (row_o[row_num] - 1) * (col_o[col_num] - 1)
print(ans)