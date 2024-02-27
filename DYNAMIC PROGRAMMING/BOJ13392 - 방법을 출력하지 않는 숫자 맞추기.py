'''
BOJ 13392 - Number Matching (Without Method) (https://www.acmicpc.net/problem/13392)

There are N rotatable number discs.
Each disc has 10 sides numbered from 1 to 10.
When you rotate a disc to the left, every disc below it rotates together with the disc.
When you rotate a disc to the right, only the disc rotates.
Given two statuses, A and B, print the minimum number of rotations to construct B from A.
'''

import sys


# 2. FUNCTIONS FOR ROTATION

def left_count(now_num, goal_num):
    
    if goal_num >= now_num:
        return goal_num - now_num
    else:
        return 10 + goal_num - now_num

def right_count(now_num, goal_num):
    
    if goal_num <= now_num:
        return now_num - goal_num
    else:
        return 10 + now_num - goal_num
        

# 1. TO GET THE INPUT

cell_count = int(sys.stdin.readline())
now = list(map(int, list(sys.stdin.readline().strip())))
goal = list(map(int, list(sys.stdin.readline().strip())))


# 3. DYNAMIC PROGRAMMING
# dp[i][j] = The minimum number of rotations to match top i cells by rotating cells to the left 10x + j times.

dp = [[float('inf') for total_left in range(10)] for cell in range(cell_count)]

for cell in range(cell_count):
    
    if cell == 0:
        
        now_num = now[cell]
        goal_num = goal[cell]
        
        add_left = left_count(now_num, goal_num)
        
        dp[cell][0] = right_count(now_num, goal_num)
        dp[cell][add_left] = add_left
    
    else:
        
        for total_left in range(10):
            
            now_num = (now[cell] + total_left) % 10
            goal_num = goal[cell]
            
            add_left = left_count(now_num, goal_num)
            
            dp[cell][total_left] = min(dp[cell][total_left], dp[cell-1][total_left] + right_count(now_num, goal_num))
            dp[cell][(total_left + add_left) % 10] = min(dp[cell][(total_left + add_left) % 10], dp[cell-1][total_left] + add_left)

print(min(dp[-1]))