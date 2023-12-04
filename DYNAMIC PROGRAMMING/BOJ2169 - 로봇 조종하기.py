'''
BOJ 2169 - Robot Control (https://www.acmicpc.net/problem/2169)

There is an N * M grid that represents the surface of Mars.
The robot starts from the top left and stops when it reaches the bottom right.
It can only move left, right, and bottom and does not visit the same cell twice.
What is the maximum value of the sum of the value of visited cells?
'''


import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = []
for row_input in range(row_count):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 2. DP
# dp[i][j][k] = Maximum score when the robot reaches grid[i][j] from direction k (0 - top, 1 - left, 2 - right)

inf = float('inf')

dp = [[[-inf, -inf, -inf] for col_num in range(col_count)] for row_num in range(row_count)]

dp[0][0] = [grid[0][0], grid[0][0], grid[0][0]]

for row_num in range(row_count):
    
    # From top
    if row_num != 0:
        for col_num in range(col_count):
            dp[row_num][col_num][0] = max(dp[row_num-1][col_num]) + grid[row_num][col_num]
    
    # From left
    for col_num in range(col_count):
        if col_num != 0:
            dp[row_num][col_num][1] = max(dp[row_num][col_num-1][0], dp[row_num][col_num-1][1]) + grid[row_num][col_num]
        
    # From right
    for col_num in range(col_count-1, -1, -1):
        if row_num != 0 and col_num != col_count - 1:
            dp[row_num][col_num][2] = max(dp[row_num][col_num+1][0], dp[row_num][col_num+1][2]) + grid[row_num][col_num]


# 3. TO SOLVE THE PROBLEM 

print(max(dp[-1][-1]))