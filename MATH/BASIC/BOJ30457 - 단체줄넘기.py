'''
BOJ 30457 - Jump Rope Team (https://www.acmicpc.net/problem/30457)

N students want to participate in a jump rope team.
Each team member can head left or right, but every member in front of her should be shorter than her. 
How many students can join the team at most?
'''

import sys


# 1. TO GET THE INPUT

student_count = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# For each height, two students at best can join the team.
# If x is the shortest height and y is the tallest, the case with the most students would be [x x+1 ... y] [y y-1 ... x]. 

height_count = [0 for index in range(1001)]

for height in students:
    height_count[height] += 1

ans = 0

for height in range(1, 1001):
    ans += min(2, height_count[height])
    
print(ans)