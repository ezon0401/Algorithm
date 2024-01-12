'''
BOJ 15240 - Paint Bucket (https://www.acmicpc.net/problem/15240)

Given a matrix of digits representing the image, simulate the result of a "fill" operation on a given pixel. 
If you apply a "fill" operation on a given pixel, adjacent pixels with the same color will be filled to a given color.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

image = []
for row_input in range(row_count):
    row = list(map(int, list(sys.stdin.readline().strip())))
    image.append(row)

target_row, target_col, target_color = map(int, sys.stdin.readline().split())


# 2. BFS

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visited = [[0 for col_num in range(col_count)] for row in range(row_count)]

start_color = image[target_row][target_col]
visited[target_row][target_col] = 1
image[target_row][target_col] = target_color
bfs = deque([(target_row, target_col)])
while bfs:
    now_row, now_col = bfs.popleft()
    for index in range(4):
        new_row, new_col = now_row + dy[index], now_col + dx[index]
        if 0 <= new_row < row_count and 0 <= new_col < col_count and visited[new_row][new_col] == 0 and image[new_row][new_col] == start_color:
            visited[new_row][new_col] = 1
            image[new_row][new_col] = target_color
            bfs.append((new_row, new_col))

for row in image:
    print("".join(map(str, row)))
    