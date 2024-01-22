'''
ABC337A - Scoreboard (https://atcoder.jp/contests/abc337/tasks/abc337_a)

Points of Team Takahashi and Team Aoki are given.
Determine the result of the match.
'''

import sys


# 1. TO GET THE INPUT

match_count = int(sys.stdin.readline())

takahashi_total = 0
aoki_total = 0

for match in range(match_count):
    takahashi_score, aoki_score = map(int, sys.stdin.readline().split())
    takahashi_total += takahashi_score
    aoki_total += aoki_score
    

# 2. TO SOLVE THE PROBLEM

if takahashi_total > aoki_total:
    print("Takahashi")
elif takahashi_total < aoki_total:
    print("Aoki")
else:
    print("Draw")