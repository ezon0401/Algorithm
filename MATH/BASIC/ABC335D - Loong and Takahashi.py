'''
ABC332D - Loong and Takahashi (https://atcoder.jp/contests/abc335/tasks/abc335_d)

There is an N X N grid. 
Construct a grid so that Takahashi is at the center, and the number x is always adjacent to x-1. 
'''


import sys


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())

grid = [[0 for index in range(size)] for index in range(size)]
grid[size // 2][size // 2] = "T"


# 2. TO SOLVE THE PROBLEM

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

row, col = 0, 0
direction = 0
num = 1
while grid[row][col] != "T":
    
    grid[row][col] = num
    
    move_row, move_col = directions[direction]
    if 0 <= row + move_row < size and 0 <= col + move_col < size and grid[row + move_row][col + move_col] == 0:
        pass
    else:
        direction = (direction + 1) % 4
        move_row, move_col = directions[direction]
    row += move_row
    col += move_col
    
    num += 1
    
for row in grid:
    print(" ".join(map(str, row)))