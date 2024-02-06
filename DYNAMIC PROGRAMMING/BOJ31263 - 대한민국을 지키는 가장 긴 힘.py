'''
BOJ 31263 - The Longest Power to Protect Korea (https://www.acmicpc.net/problem/31263)

Each soldier wrote a number between 1 and 641 consecutively without a blank.
Given a result, print the minimum number of soldiers.
'''

import sys


# 1. TO GET THE INPUT

inf = float('inf')

length = int(sys.stdin.readline())
paper = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM (DYNAMIC PROGRAMMING)
# dp[i][j] = The minimum number of soldiers until index i when paper[i] is a j-th digit.

dp = [[inf, inf, inf] for index in range(length)]
dp[0][0] = 1

for index in range(1, length):
    
    now_num = int(paper[index])

    if now_num != 0:
        dp[index][0] = min(dp[index-1]) + 1
    dp[index][1] = dp[index-1][0]
    if 0 <= index-2 and int(paper[index-2:index+1]) <= 641:
        dp[index][2] = dp[index-1][1]
    
print(min(dp[-1]))