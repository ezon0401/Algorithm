'''
BOJ 10254 - Highway (https://www.acmicpc.net/problem/10254)

Given N points on a 2D plane, print the two farthest coordinates.
'''

import sys


# 2. A CCW FUNCTION

def ccw(point1, point2, point3):
    
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3 


# 4. A FUNCTION TO GET DISTANCE

def distance_squared(point1, point2):
    
    x1, y1 = point1
    x2, y2 = point2
    
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    points = []
    
    city_count = int(sys.stdin.readline())
    for city in range(city_count):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x, y))
    points.sort()
    
    
    # 3. MONOTONE CHAIN
    
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
    
    
    # 5. ROTATING CALIPERS
    
    max_dist = 0
    ans = None
    
    upper_index = 0
    lower_index = len(lower_hull) - 1
    
    while True:
        
        dist = distance_squared(upper_hull[upper_index], lower_hull[lower_index])
        if dist > max_dist:
            max_dist = dist
            ans = (upper_hull[upper_index], lower_hull[lower_index])
        
        if upper_index == len(upper_hull) - 1:
            if lower_index == 0:
                break
            else:
                lower_index -= 1
        elif lower_index == 0:
            upper_index += 1
        else:
            
            upper_delta_x = upper_hull[upper_index+1][0] - upper_hull[upper_index][0]            
            upper_delta_y = upper_hull[upper_index+1][1] - upper_hull[upper_index][1] 
            lower_delta_x = lower_hull[lower_index][0] - lower_hull[lower_index-1][0]
            lower_delta_y = lower_hull[lower_index][1] - lower_hull[lower_index-1][1]
            
            if upper_delta_y * lower_delta_x > lower_delta_y * upper_delta_x:
                upper_index += 1
            else:
                lower_index -= 1
    
    for point in ans:
        print(point[0], point[1], end = ' ')
    print()