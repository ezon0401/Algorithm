'''
BOJ 21938 - Image Processing (https://www.acmicpc.net/problem/21938)

An image consists of N * M pixels. The pixel (i, j) contains RGB values.
A pixel converts to black if the average of three color values is higher than the threshold value. Otherwise, it converts to white.
Adjacent black pixels on the converted image are recognized as the same object.
Determine how many objects are there in the converted image.
'''

import sys
from collections import deque


# 2. FUNCTIONS TO CONVERT AN IMAGE

def image_conversion(image):
    
    new_image = []
    for row in image:
        new_image.append(row_conversion(row))
    return new_image
            
def row_conversion(row):
    
    new_row = []
    for pixel_input in range(column_count):
        
        rgb_sum = 0
        for rgb_index in range(pixel_input * 3, pixel_input * 3 + 3):
            rgb_sum += row[rgb_index]
            
        if rgb_sum >= 3 * threshold:
            new_row.append(255)
        else:
            new_row.append(0)
            
    return new_row


# 3. BFS FUNCTION

def bfs(row_num, column_num):
    
    queue = deque([(row_num, column_num)])
    while queue:
        now_row, now_column = queue.popleft()
        for index in range(4):
            new_row = now_row + dy[index]
            new_column = now_column + dx[index]
            if 0 <= new_row < row_count and 0 <= new_column < column_count and visited[new_row][new_column] == 0 and new_image[new_row][new_column] == 255:
                visited[new_row][new_column] = 1
                queue.append((new_row, new_column))


# 1. TO GET THE INPUT

row_count, column_count = map(int, sys.stdin.readline().split())

image = []
for row_input in range(row_count):
    row = list(map(int, sys.stdin.readline().split()))
    image.append(row)

threshold = int(sys.stdin.readline())


# 4. TO SOLVE THE PROBLEM

object_count = 0

new_image = image_conversion(image)
visited = [[0 for column_num in range(column_count)] for row_num in range(row_count)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for row_num in range(row_count):
    for column_num in range(column_count):
        if visited[row_num][column_num] == 0 and new_image[row_num][column_num] == 255:
            visited[row_num][column_num] = 1
            bfs(row_num, column_num)
            object_count += 1

print(object_count)