'''
BOJ 30167 - Dao's race (https://www.acmicpc.net/problem/30166)

There is an array of scores of N tracks. The goal is to make an increasing array.
It is possible to do the following operation: Choose one index i and increase the index by K.
You can only execute the operation once for each index. 
Determine the minimum number of operations needed. 
'''

import sys


# 1. TO SOLVE THE PROBLEM

track_count, length = map(int, sys.stdin.readline().split())
tracks = list(map(int, sys.stdin.readline().split()))

possible = True
count = 0
for index in range(1, track_count):
    if tracks[index-1] >= tracks[index]:
        if tracks[index-1] >= tracks[index] + length:
            possible = False
            break
        else:
            tracks[index] += length
            count += 1

if possible:
    print(count)
else:
    print(-1)