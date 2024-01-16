'''
BOJ 1708 - Convex Hull (https://www.acmicpc.net/problem/1708)

Given N points on a 2D plane, print the number of points on the convex hull.
'''

import sys


# 2. FUNCTIONS FOR GRAHAM SCAN

def slope(point1, point2):
    
    if point1[0] == point2[0]:
        return float('inf')
    else:
        return (point1[1] - point2[1]) / (point1[0] - point2[0])
        
def ccw(point1, point2, point3):
    
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


# 1. TO GET THE INPUT

point_count = int(sys.stdin.readline())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
points.sort(reverse=True)


# 3. GRAHAM SCAN

start = points.pop()
convex_hull = [start]

points.sort(key = lambda x : (slope(start, x), x[0], x[1]))

for point in points:
    while len(convex_hull) > 1 and ccw(convex_hull[-2], convex_hull[-1], point) <= 0:
        convex_hull.pop()
    convex_hull.append(point)

print(len(convex_hull))