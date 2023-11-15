'''
BOJ 22503 - Tiles are Colorful (https://www.acmicpc.net/problem/22503)

There is an N * M grid. "." indicates there is no tile in a cell, and an alphabet character indicates the color of a tile.
Rabbit can perform an operation with the following steps infinite times:

(1) Choose an empty cell.
(2) Search upward until she finds a cell with a tile. The cell is now a focus cell for an operation.
(3) Search downward, leftward, and rightward in the same way. Rabbit will have at most 4 focus cells.
(4) If there is a pair of focus cells with the same alphabet, eliminate both of them from the grid.
(5) Rabbit earns a point that is equal to the number of eliminated tiles.

Determine the maximum point Rabbit can earn.
'''

import sys


# 2. FUNCTIONS FOR OPERATION

def operation():
    
    global score
    
    for alphabet in alphabet_loc:
        
        row1, col1 = alphabet[0]
        row2, col2 = alphabet[1]
        
        if row1 != row2 and col1 != col2:
            focus1 = get_focus(row1, col2)
            focus2 = get_focus(row2, col1)
            if ((row1, col1) in focus1 and (row2, col2) in focus1) or ((row1, col1) in focus2 and (row2, col2) in focus2):
                grid[row1][col1] = "."
                grid[row2][col2] = "."
                score += 2
        else:
            if row1 == row2:
                focus = get_focus(row1, min(col1, col2) + 1)
            if col1 == col2:
                focus = get_focus(min(row1, row2) + 1, col1)
            if (row1, col1) in focus and (row2, col2) in focus:
                    grid[row1][col1] = "."
                    grid[row2][col2] = "."
                    score += 2        
        
def get_focus(row_num, col_num):
    
    focus = []
    
    row_direction = [-1, 1, 0, 0]
    col_direction = [0, 0, -1, 1]
    
    for index in range(4):
        row_now, col_now = row_num, col_num
        while 0 <= row_now < row_count and 0 <= col_now < col_count and grid[row_now][col_now] == ".":
            row_now += row_direction[index]
            col_now += col_direction[index]
        if 0 <= row_now < row_count and 0 <= col_now < col_count and grid[row_now][col_now] != ".":
            focus.append((row_now, col_now))
    
    return focus
    
    
# 1. TO GET INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

alphabet_loc = [[(-1, -1), (-1, -1)] for alphabet in range(26)]

grid = []
for row_num in range(row_count):
    row = list(sys.stdin.readline().strip())
    grid.append(row)
    
    for col_num in range(col_count):
        if row[col_num] != ".":
            alphabet = ord(row[col_num]) - 65
            if alphabet_loc[alphabet][0] == (-1, -1):
                alphabet_loc[alphabet][0] = (row_num, col_num)
            else:
                alphabet_loc[alphabet][1] = (row_num, col_num)


# 3. TO SOLVE THE PROBLEM
# Rabbit can perform at most 26 operations that brings change.

score = 0
for alphabet in range(26):
    operation()
print(score)