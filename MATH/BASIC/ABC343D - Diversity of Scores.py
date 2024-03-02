'''
ABC343D - Diversity of Scores (https://atcoder.jp/contests/abc343/tasks/abc343_d)

The scores of players change every second.
At every second, print the number of distinct scores.
'''

import sys


# 1. TO GET THE INPUT

player_count, time_count = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

score_count = {0:player_count}
score = [0 for index in range(player_count)]

ans = 1

for time in range(time_count):
    
    player, point = map(int, sys.stdin.readline().split())
    player -= 1
    
    player_score = score[player]
    
    score_count[player_score] -= 1
    if score_count[player_score] == 0:
        ans -= 1
    
    if player_score + point not in score_count:
        score_count[player_score + point] = 1
        ans += 1
    else:
        score_count[player_score + point] += 1
        if score_count[player_score + point] == 1:
            ans += 1
    
    score[player] = player_score + point
    
    print(ans)