'''
BOJ 7420 - Protection Wall (https://www.acmicpc.net/problem/7420)

An architect wants to build a protection wall that does not come closer to buildings than a distance L.
Given L and coordinates of buildings, print the minimum length of the wall.
'''

import sys
from math import pi


# 2. A CCW FUNCTION

def ccw(point1, point2, point3):
    
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


# 4. FUNCTIONS TO SOLVE THE PROBLEM

def get_dist(point1, point2):
    
    x1, y1 = point1
    x2, y2 = point2
    
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)

def my_round(num):
    
    if int(num * 2) == int(num) * 2:
        return int(num)
    else:
        return int(num) + 1


# 1. TO GET THE INPUT

point_count, length = map(int, sys.stdin.readline().split())

points = []
for point in range(point_count):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
points.sort()


# 3. MONOTONE SCAN

upper_hull = []
for point in points:
    while len(upper_hull) > 1 and ccw(upper_hull[-2], upper_hull[-1], point) >= 0:
        upper_hull.pop()
    upper_hull.append(point)

lower_hull = []
for point in points:
    while len(lower_hull) > 1 and ccw(lower_hull[-2], lower_hull[-1], point) <= 0:
        lower_hull.pop()
    lower_hull.append(point)

convex_hull = []
for index in range(len(upper_hull)):
    convex_hull.append(upper_hull[index])
for index in range(len(lower_hull) - 2, 0, -1):
    convex_hull.append(lower_hull[index])


# 5. TO SOLVE THE PROBLEM

convex_hull.append(convex_hull[0])

ans = 0

for index in range(len(convex_hull) - 1):
    
    point1 = convex_hull[index]
    point2 = convex_hull[index+1]
    
    ans += get_dist(point1, point2)

# The sum of all remaining angles must be 360. 
ans += 2 * length * pi

print(my_round(ans))