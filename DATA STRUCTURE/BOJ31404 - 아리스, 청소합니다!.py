'''
BOJ 31404 - Aris cleans! (https://www.acmicpc.net/problem/31404)

A H X W grid is given. Aris is at (R, C) and facing direction X.
Two grids, A and B, describe rules: how much to rotate.

Aris repeats the following operations:

(1) If there is dust at the current location, remove it.
(2) If she removed dust right before, follow rule A. If not, follow rule B.
(3) Move by 1 to the current facing direction.

Aris will stop cleaning if she leaves a grid or there is no possibility to remove dust anymore.
Print how many times Aris will repeat the operations.
'''

import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())
now_row, now_col, now_face = map(int, sys.stdin.readline().split())

rule_A = []
for row_input in range(row_count):
    row = list(sys.stdin.readline().strip())
    row = list(map(int, row))
    rule_A.append(row)

rule_B = []
for row_input in range(row_count):
    row = list(sys.stdin.readline().strip())
    row = list(map(int, row))
    rule_B.append(row)


# 2. TO SOLVE THE PROBLEM
# If Aris removes dust, an array that checks whether a state is visited must be reset.

direction_y = [-1, 0, 1, 0]
direction_x = [0, 1, 0, -1]

save = []
count = 0

dust = [[1 for col in range(col_count)] for row in range(row_count)]
second = [[[0, 0, 0, 0] for col in range(col_count)] for row in range(row_count)]

while True:
    
    count += 1
    
    if dust[now_row][now_col] == 1:
        
        dust[now_row][now_col] = 0
        now_face = (now_face + rule_A[now_row][now_col]) % 4
        while save:
            row, col, face = save.pop()
            second[row][col][face] = 0
        
    else:
        
        second[now_row][now_col][now_face] = 1
        save.append((now_row, now_col, now_face))
        now_face = (now_face + rule_B[now_row][now_col]) % 4

    now_row += direction_y[now_face]
    now_col += direction_x[now_face]
    
    if not (0 <= now_row < row_count and 0 <= now_col < col_count):
        break
    if second[now_row][now_col][now_face] == 1:
        break

print(count - len(save))