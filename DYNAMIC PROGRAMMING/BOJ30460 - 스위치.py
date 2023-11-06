'''
BOJ 30460 - Switch (https://www.acmicpc.net/problem/30460)

A player can get a score A_i at second i.
If the player presses the switch at second T, he doubles the point for second T ~ T+2.
The player can press the switch again at T+3.
Determine the maximum score the player can get.
'''

import sys


# 1. TO GET THE INPUT

second_count = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# dp[T] = The maximum score the player can get until the second T when the switch is [pressed at T, pressed at T-1, pressed at T-2, not pressed].

dp = [[0, 0, 0, 0] for second in range(second_count)]

for second in range(second_count):
    if second == 0:
        dp[second] = [score[0] * 2, score[0], score[0], score[0]]
    elif second == 1:
        dp[second] = [score[0] + score[1] * 2, score[0] * 2 + score[1] * 2, score[0] + score[1], score[0] + score[1]]
    else:
        dp[second] = [max(dp[second-1][2], dp[second-1][3]) + score[second] * 2, dp[second-1][0] + score[second] * 2, dp[second-1][1] + score[second] * 2, max(dp[second-1][2], dp[second-1][3]) + score[second]]
        
print(max(dp[-1]))