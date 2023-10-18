'''
BOJ 14939 - Turn off the lights (https://www.acmicpc.net/problem/14939)

There are 100 light bulbs in a 10 * 10 board, either turned on [O] or off [#].
If you press the switch of a light bulb, the light bulb and the adjacent 4 light bulbs will change its status.

Determine if it is possible to turn off all light bulbs.
If possible, print the minimum number of presses. Otherwise, print -1.
'''

import sys


# 2. FUNCTIONS TO HELP SOLVING THE PROBLEM

# A function to change a status of a light bulb

def change_status(status):
    if status == "O":
        return "#"
    else:
        return "O"

# A function to press a light bulb and return a board after the press
# Deep-copied the board just in case

def press(board, row_num, column_num):
    
    board = [row[:] for row in board]
    
    board[row_num][column_num] = change_status(board[row_num][column_num])
    if 0 <= column_num-1:
        board[row_num][column_num-1] = change_status(board[row_num][column_num-1])
    if column_num+1 < 10:
        board[row_num][column_num+1] = change_status(board[row_num][column_num+1])
    if 0 <= row_num-1:
        board[row_num-1][column_num] = change_status(board[row_num-1][column_num])
    if row_num+1 < 10:
        board[row_num+1][column_num] = change_status(board[row_num+1][column_num])
    
    return board
    
# A function to check if there is no light

def no_light(board):
    
    check = True
    for row_num in range(10):
        for column_num in range(10):
            if board[row_num][column_num] == "O":
                check = False
                break
    return check            


# 1. TO GET THE INPUT

board = []
for row_input in range(10):
    row = list(sys.stdin.readline().strip())
    board.append(row)


# 3. TO SOLVE THE PROBLEM

# It is unnecessary to press the same switch more than once. 
# There can be total (2 ^ 100) cases, yet let's only focus on the first row for now.
# Bit-masking is helpful to consider all (2 ^ 10) cases: 111111111 for all light bulbs pressed, 00000000 for no light bulbs pressed.
# Don't forget to deep-copy the board.

cases = []

for case in range(1024):    
    
    press_count = 0
    
    board_copy = [row[:] for row in board]
    for lightbulb in range(10):
        if case & (1 << lightbulb):
            press_count += 1
            board_copy = press(board_copy, 0, lightbulb)
            
    cases.append((press_count, board_copy))

# Now, we have every case possible for the first row.
# Then what light bulbs should we press for the next 9 rows?
# In each case, if board[row-1][column] is on, the board[row][column] should be pressed since it is the only way to turn off the light bulb we've gone through.
# If there is a light after going through all rows, the case cannot turn off all the lights.

ans = -1

for case in cases:
    
    press_count, board = case

    for row_num in range(1, 10):
        for column_num in range(10):
            if board[row_num-1][column_num] == "O":
                press_count += 1
                board = press(board, row_num, column_num)
    
    if no_light(board) and (ans == -1 or ans > press_count):
        ans = press_count
    
print(ans)