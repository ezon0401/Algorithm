'''
BOJ 6788 - All Your Base (https://www.acmicpc.net/problem/6788)

The average rank for each of the scores is given.
Print the exact range in which the given score falls.
'''

import sys


# 1. TO GET INPUT

info_count = int(sys.stdin.readline())

info = []
for info_input in range(info_count):
    score, rank = map(float, sys.stdin.readline().split())
    info.append((score, rank))
info.sort(reverse=True)

target_score = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM
# We can determine each score range by starting from the highest rank.

now = 1
for score, rank in info:
    best = now
    worst = rank * 2 - now
    if score == target_score:
        print(int(best))
        print(int(worst))
        break
    else:
        now = worst + 1