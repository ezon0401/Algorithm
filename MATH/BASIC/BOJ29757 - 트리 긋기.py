'''
BOJ 29757 - Draw a Tree (https://www.acmicpc.net/problem/29757)

Given points, draw a tree.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

point_count = int(sys.stdin.readline())

point = []
for point_num in range(1, point_count + 1):
    x, y = map(int, sys.stdin.readline().split())
    point.append((x, y, point_num))
point.sort()

for index in range(1, len(point)):
    print(point[index-1][-1], point[index][-1])