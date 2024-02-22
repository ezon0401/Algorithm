'''
BOJ 12869 - Mutalisk (https://www.acmicpc.net/problem/12869)

Mutalisk attacks 3 SCVs at once.
SCVs attacked first, second, and third are damaged 9, 3, 1, respectively.
Determine a minimum number of attacks to kill all SCVs.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

scv_count = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

start = [0, 0, 0]
for index in range(scv_count):
    start[index] = arr[index]


# 2. TO SOLVE THE PROBLEM

visited = [[[-1 for scv3 in range(61)] for scv2 in range(61)] for scv1 in range(61)]
visited[start[0]][start[1]][start[2]] = 0

move = [(-9, -3, -1), (-9, -1, -3), (-3, -1, -9), (-3, -9, -1), (-1, -9, -3), (-1, -3, -9)]

queue = deque([start])
while queue:
    scv1, scv2, scv3 = queue.popleft()
    for delta_scv1, delta_scv2, delta_scv3 in move:
        new_scv1 = max(scv1 + delta_scv1, 0)
        new_scv2 = max(scv2 + delta_scv2, 0)
        new_scv3 = max(scv3 + delta_scv3, 0)
        if new_scv1 == 0 and new_scv2 == 0 and new_scv3 == 0:
            print(visited[scv1][scv2][scv3] + 1)
            sys.exit(0)
        else:
            if visited[new_scv1][new_scv2][new_scv3] == -1:
                visited[new_scv1][new_scv2][new_scv3] = visited[scv1][scv2][scv3] + 1
                queue.append([new_scv1, new_scv2, new_scv3])
    