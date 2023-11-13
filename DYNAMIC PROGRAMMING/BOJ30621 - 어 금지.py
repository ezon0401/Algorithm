'''
BOJ 30621 - "Oh?" Not Allowed (https://www.acmicpc.net/problem/30621)

Sung-woo can shout "Oh?" to get points.
If he has not shouted since (t_i - b_i), he can shout at t_i.
He earns c_i points when shouts at t_i.
Determine the maximum point Sung-woo can earn.
'''

import sys
from bisect import bisect_left


# 1. TO GET THE INPUT

time_count = int(sys.stdin.readline())

time = list(map(int, sys.stdin.readline().split()))
cooldown = list(map(int, sys.stdin.readline().split()))
score = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# dp[i] = The maximum point Sung-woo can earn until the index i.

dp = [0 for index in range(time_count)]
dp[0] = score[0]

for index in range(1, time_count):
    
    now_score = 0
    last_shout = bisect_left(time, time[index] - cooldown[index]) - 1 
    if last_shout >= 0:
        now_score = dp[last_shout]
    
    dp[index] = max(dp[index-1], now_score + score[index])

print(dp[-1])