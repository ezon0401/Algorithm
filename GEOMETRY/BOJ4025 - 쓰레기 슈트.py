'''
BOJ 4025 - Trash Chute (https://www.acmicpc.net/problem/4025)

Given a polygon, determine the minimum length of a trash chute to put the polygon inside.
'''

import sys
from decimal import Decimal
from math import ceil


# 2. CCW

def ccw(point1, point2, point3):
    
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    

# 4. A FUNCTION TO GET THE DISTANCE BETWEEN A SEGMENT AND A POINT

def seg_to_point(seg_pointA, seg_pointB, point):
    
    x1, y1 = seg_pointA
    x2, y2 = seg_pointB
    
    area = abs(ccw(seg_pointA, seg_pointB, point))
    seg_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** Decimal('0.5')
    
    return area / seg_length


# 1. TO GET THE INPUT

test = 1

while True:
    
    point_count = int(sys.stdin.readline())
    if point_count == 0:
        break
    
    points = []
    for point in range(point_count):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    points.sort()
    
    
    # 3. CONVEX HULL - MONOTONE CHAIN
    
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
    
    convex_hull = upper_hull + lower_hull[-2:0:-1]
    
    
    # 4. TO SOLVE THE PROBLEM
    # The answer equals to the minimum length between a segment and its farthest point.
    
    convex_hull.append(convex_hull[0])
    
    ans = float('inf')
    for i in range(len(convex_hull) - 1):
        longest = 0
        for j in range(len(convex_hull)):
            distance = seg_to_point(convex_hull[i], convex_hull[i+1], convex_hull[j])
            longest = max(longest, distance)
        ans = min(ans, longest)

    ans = ceil(ans * 100) / Decimal('100')
        
    print("Case %d: %.2f" % (test, ans))
    test += 1