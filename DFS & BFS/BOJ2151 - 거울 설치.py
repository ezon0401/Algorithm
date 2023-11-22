'''
BOJ 2151 - Mirror Positioning (https://www.acmicpc.net/problem/2151)

There is a room with 2 doors: "#" is a door, "." is an empty cell, "*" is a wall, and "!" is where a two-way mirror can be positioned.
The goal is to see the other door from one door using two-way mirrors.
Determine the minimum number of mirrors required.
'''

import sys
from collections import deque


# 2. BFS
# visited[R][C][X] = The minimum number of mirrors required to reach (R, C) with a direction X.

def bfs(row_num, col_num):
    
    move_row = [-1, 1, 0, 0]
    move_col = [0, 0, -1, 1]
    
    queue = deque([])
    
    # Starting points
    for direction in range(4):
        visited[row_num][col_num][direction] = 0
        new_row = row_num + move_row[direction]
        new_col = col_num + move_col[direction]
        if 0 <= new_row < house_size and 0 <= new_col < house_size:
            queue.append((new_row, new_col, direction))
            visited[new_row][new_col][direction] = 0
    
    while queue:
        
        now_row, now_col, direction = queue.popleft()
        
        # Light cannot penetrate walls and doors.
        if house[now_row][now_col] == "*" or house[now_row][now_col] == "#":
            continue
        
        # Light can only move straight at an empty cell.
        elif house[now_row][now_col] == ".":
            new_row = now_row + move_row[direction]
            new_col = now_col + move_col[direction]
            if 0 <= new_row < house_size and 0 <= new_col < house_size and visited[now_row][now_col][direction] < visited[new_row][new_col][direction]:
                queue.append((new_row, new_col, direction))
                visited[new_row][new_col][direction] = visited[now_row][now_col][direction]
                
        # Otherwise, light can either move straight or be refracted by a two-way mirror.
        else:
            for new_direction in range(4):
                new_row = now_row + move_row[new_direction]
                new_col = now_col + move_col[new_direction]
                if 0 <= new_row < house_size and 0 <= new_col < house_size:
                    if direction == new_direction and visited[now_row][now_col][direction] < visited[new_row][new_col][new_direction]:
                        queue.append((new_row, new_col, new_direction))
                        visited[new_row][new_col][new_direction] = visited[now_row][now_col][direction]
                    if direction != new_direction and visited[now_row][now_col][direction] + 1 < visited[new_row][new_col][new_direction]:
                        queue.append((new_row, new_col, new_direction))
                        visited[new_row][new_col][new_direction] = visited[now_row][now_col][direction] + 1
                
    

# 1. TO GET INPUT    

house_size = int(sys.stdin.readline())

house = []
for row_input in range(house_size):
    row = list(sys.stdin.readline().strip())
    house.append(row)


# 3. TO SOLVE THE PROBLEM

inf = float('inf')
started = False
visited = [[[inf, inf, inf, inf] for col_num in range(house_size)] for row_num in range(house_size)]

for row_num in range(house_size):
    for col_num in range(house_size):
        if house[row_num][col_num] == "#":
            if started == False:
                bfs(row_num, col_num)
                started = True
            else:
                print(min(visited[row_num][col_num]))