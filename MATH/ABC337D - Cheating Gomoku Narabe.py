'''
ABC337D - Cheating Gomoku Narabe (https://atcoder.jp/contests/abc337/tasks/abc337_d)

There is a H X W grid consisting of 'o', 'x', or '.'.
You can choose one cell with '.' and change it to 'o' with an operation.
Determine if it is possible to have a consecutive sequence of K 'o's horizontally or vertically.
If possible, print the minimum number of operations. 
'''

import sys


# 2. FUNCTIONS TO ADD OR REMOVE VALUE IN ARRAY

def add_count(arr, row, col, char):
    if char == "o":
        arr[row][col][0] += 1
    elif char == "x":
        arr[row][col][1] += 1
    else:
        arr[row][col][2] += 1

def remove_count(arr, row, col, char):
    if char == "o":
        arr[row][col][0] -= 1
    elif char == "x":
        arr[row][col][1] -= 1
    else:
        arr[row][col][2] -= 1


# 1. TO GET THE INPUT

row_count, col_count, length = map(int, sys.stdin.readline().split())

grid = []
for row_input in range(row_count):
    row = list(sys.stdin.readline().strip())
    grid.append(row)


# 3. SLIDING WINDOW

# An array to check each row: [Number of o, number of x, number of .]

row_check = [[[0, 0, 0] for col in range(col_count)] for row in range(row_count)]
for row in range(row_count):
    for col in range(col_count):
        char = grid[row][col]
        if col == 0:
            add_count(row_check, row, col, char)
        elif col < length:
            row_check[row][col] = row_check[row][col-1][:]
            add_count(row_check, row, col, char)
        else:
            row_check[row][col] = row_check[row][col-1][:]
            add_count(row_check, row, col, char)
            remove_count(row_check, row, col, grid[row][col-length])

# An array to check each column

col_check = [[[0, 0, 0] for col in range(col_count)] for row in range(row_count)]
for row in range(row_count):
    for col in range(col_count):
        char = grid[row][col]
        if row == 0:
            add_count(col_check, row, col, char)
        elif row < length:
            col_check[row][col] = col_check[row-1][col][:]
            add_count(col_check, row, col, char)
        else:
            col_check[row][col] = col_check[row-1][col][:]
            add_count(col_check, row, col, char)
            remove_count(col_check, row, col, grid[row-length][col])


# 4. TO SOLVE THE PROBLEM

ans = float('inf')

for row in range(row_count):
    for col in range(length-1, col_count):
        if row_check[row][col][1] == 0:
            ans = min(ans, row_check[row][col][2])
            
for row in range(length-1, row_count):
    for col in range(col_count):
        if col_check[row][col][1] == 0:
            ans = min(ans, col_check[row][col][2])
            
if ans == float('inf'):
    print(-1)
else:
    print(ans)


