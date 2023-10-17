'''
BOJ 13460 - Labyrinth 2 (https://www.acmicpc.net/problem/13460)

There is an N * M board with walls [#], a hole [O], a red marble [R], and a blue marble [B].
The goal is to put the red marble into the hole without putting the blue marble into the hole.
You can tilt the board in four directions: leftward, rightward, frontward, and backward.

Determine whether it is possible to clear the game within 10 tilts.
If possible, print the minimum number of tilts needed.
Otherwise, print -1.
'''

import sys
from collections import deque


# 2. FUNCTIONS TO IMPLEMENT TILTS

# Find the locations of the marbles on the board.

def find_marbles(board):
    
    red_row, red_col, blue_row, blue_col = None, None, None, None
    
    for row_num in range(row_count):
        for col_num in range(col_count):
            if board[row_num][col_num] == "R":
                red_row, red_col = row_num, col_num
            if board[row_num][col_num] == "B":
                blue_row, blue_col = row_num, col_num
                
    return red_row, red_col, blue_row, blue_col

# Tilts
# Move the red marble first, then the blue marble. Since the blue marble may have blocked the red marble, the red marble should be moved again.
# Make sure that the board is deep-copied.

# Tilt leftward

def tilt_left(now_board):
    
    board = [row[:] for row in now_board]
    red_row, red_col, blue_row, blue_col = find_marbles(board)
    
    while 0 <= red_col - 1 and board[red_row][red_col-1] == ".":
        board[red_row][red_col], board[red_row][red_col-1] = board[red_row][red_col-1], board[red_row][red_col]
        red_col -= 1
    if 0 <= red_col - 1 and board[red_row][red_col-1] == "O":
        board[red_row][red_col] = "."
    
    while 0 <= blue_col - 1 and board[blue_row][blue_col-1] == ".":
        board[blue_row][blue_col], board[blue_row][blue_col-1] = board[blue_row][blue_col-1], board[blue_row][blue_col]
        blue_col -= 1
    if 0 <= blue_col - 1 and board[blue_row][blue_col-1] == "O":
        board[blue_row][blue_col] = "."
    
    while 0 <= red_col - 1 and board[red_row][red_col-1] == ".":
        board[red_row][red_col], board[red_row][red_col-1] = board[red_row][red_col-1], board[red_row][red_col]
        red_col -= 1
    if 0 <= red_col - 1 and board[red_row][red_col-1] == "O":
        board[red_row][red_col] = "."

    return board

# Tilt rightward

def tilt_right(now_board):
    
    board = [row[:] for row in now_board]
    red_row, red_col, blue_row, blue_col = find_marbles(board)
    
    while red_col + 1 < col_count and board[red_row][red_col+1] == ".":
        board[red_row][red_col], board[red_row][red_col+1] = board[red_row][red_col+1], board[red_row][red_col]
        red_col += 1
    if red_col + 1 < col_count and board[red_row][red_col+1] == "O":
        board[red_row][red_col] = "."
        
    while blue_col + 1 < col_count and board[blue_row][blue_col+1] == ".":
        board[blue_row][blue_col], board[blue_row][blue_col+1] = board[blue_row][blue_col+1], board[blue_row][blue_col]
        blue_col += 1
    if blue_col + 1 < col_count and board[blue_row][blue_col+1] == "O":
        board[blue_row][blue_col] = "."
        
    red_col = red_col
    while red_col + 1 < col_count and board[red_row][red_col+1] == ".":
        board[red_row][red_col], board[red_row][red_col+1] = board[red_row][red_col+1], board[red_row][red_col]
        red_col += 1
    if red_col + 1 < col_count and board[red_row][red_col+1] == "O":
        board[red_row][red_col] = "."

    return board

# Tilt backward

def tilt_back(now_board):
        
    board = [row[:] for row in now_board]
    red_row, red_col, blue_row, blue_col = find_marbles(board)
    
    while 0 <= red_row - 1 and board[red_row-1][red_col] == ".":
        board[red_row-1][red_col], board[red_row][red_col] = board[red_row][red_col], board[red_row-1][red_col]
        red_row -= 1
    if 0 <= red_row - 1 and board[red_row-1][red_col] == "O":
        board[red_row][red_col] = "."
        
    while 0 <= blue_row - 1 and board[blue_row-1][blue_col] == ".":
        board[blue_row-1][blue_col], board[blue_row][blue_col] = board[blue_row][blue_col], board[blue_row-1][blue_col]
        blue_row -= 1
    if 0 <= blue_row - 1 and board[blue_row-1][blue_col] == "O":
        board[blue_row][blue_col] = "."
        
    red_row = red_row
    while 0 <= red_row - 1 and board[red_row-1][red_col] == ".":
        board[red_row-1][red_col], board[red_row][red_col] = board[red_row][red_col], board[red_row-1][red_col]
        red_row -= 1
    if 0 <= red_row - 1 and board[red_row-1][red_col] == "O":
        board[red_row][red_col] = "."

    return board

# Tilt frontward

def tilt_front(now_board):
    
    board = [row[:] for row in now_board]
    red_row, red_col, blue_row, blue_col = find_marbles(board)
    
    while red_row + 1 < row_count and board[red_row+1][red_col] == ".":
        board[red_row+1][red_col], board[red_row][red_col] = board[red_row][red_col], board[red_row+1][red_col]
        red_row += 1
    if red_row + 1 < row_count and board[red_row+1][red_col] == "O":
        board[red_row][red_col] = "."
        
    while blue_row + 1 < row_count and board[blue_row+1][blue_col] == ".":
        board[blue_row+1][blue_col], board[blue_row][blue_col] = board[blue_row][blue_col], board[blue_row+1][blue_col]
        blue_row += 1
    if blue_row + 1 < row_count and board[blue_row+1][blue_col] == "O":
        board[blue_row][blue_col] = "."
        
    red_row = red_row
    while red_row + 1 < row_count and board[red_row+1][red_col] == ".":
        board[red_row+1][red_col], board[red_row][red_col] = board[red_row][red_col], board[red_row+1][red_col]
        red_row += 1
    if red_row + 1 < row_count and board[red_row+1][red_col] == "O":
        board[red_row][red_col] = "."

    return board


# 3. FUNCTIONS TO CHECK WHETHER THE GAME IS CLEARED

# Check whether the red marble entered the hole

def red_in_hole(board):
    
    hole = True
    
    for row_num in range(row_count):
        for col_num in range(col_count):
            if board[row_num][col_num] == "R":
                hole = False
                break
    
    return hole
    
# Check whether the blue marble entered the hole
    
def blue_in_hole(board):
    
    hole = True
    
    for row_num in range(row_count):
        for col_num in range(col_count):
            if board[row_num][col_num] == "B":
                hole = False
                break
    
    return hole
    

# 4. A FUNCTION TO CONVERT THE BOARD INTO A STRING

def to_string(board):
    
    key = ""
    for row in board:
        key += "".join(row)
    
    return key


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

board = []
for row_input in range(row_count):
    row = list(sys.stdin.readline().strip())
    board.append(row)


# 5. TO SOLVE THE PROBLEM (BFS)
# The list state_checked eliminates redundant operations by storing each board status.

ans = -1
state_checked = set()

bfs = deque([(0, board)])
while bfs:
    
    now_count, now_board = bfs.popleft()
    now_string = to_string(now_board)
    
    if now_string not in state_checked:
        
        state_checked.add(now_string)
        
        if not blue_in_hole(now_board):
            if red_in_hole(now_board):
                ans = now_count
                break
            else:
                if now_count < 10:
                    bfs.append((now_count + 1, tilt_left(now_board)))
                    bfs.append((now_count + 1, tilt_right(now_board)))
                    bfs.append((now_count + 1, tilt_back(now_board)))
                    bfs.append((now_count + 1, tilt_front(now_board)))

print(ans)