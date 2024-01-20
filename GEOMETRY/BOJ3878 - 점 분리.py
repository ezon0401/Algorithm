'''
BOJ 3878 - Point Separation (https://www.acmicpc.net/problem/3878)

There are N white points and M black points on a 2D plane.
Determine whether it is possible to separate white points from black points with a straight line.
'''


import sys


# 2. CCW FUNCTION

def ccw(point1, point2, point3):
    
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    
    return x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3


# 3. MONOTONE CHAIN

def convex_hull(points):
    
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
    
    return upper_hull + lower_hull[-2:0:-1]


# 4. FUNCTIONS TO SOLVE THE PROBLEM

def point_on_line(point, line):
    
    result = False
    if ccw(line[0], line[1], point) == 0 and min(line[0][0], line[1][0]) <= point[0] <= max(line[0][0], line[1][0]) and min(line[0][1], line[1][1]) <= point[1] <= max(line[0][1], line[1][1]):
        result = True
    return result

def line_intersection(lineA, lineB):
    
    lineA_ccw_result1 = ccw(lineA[0], lineA[1], lineB[0])
    lineA_ccw_result2 = ccw(lineA[0], lineA[1], lineB[1])
    
    lineB_ccw_result1 = ccw(lineB[0], lineB[1], lineA[0])
    lineB_ccw_result2 = ccw(lineB[0], lineB[1], lineA[1])
    
    result = False
    if lineA_ccw_result1 * lineA_ccw_result2 < 0 and lineB_ccw_result1 * lineB_ccw_result2 < 0:
        result = True
    else:
        if lineA_ccw_result1 == 0 and point_on_line(lineB[0], lineA):
            result = True
        if lineA_ccw_result2 == 0 and point_on_line(lineB[1], lineA):
            result = True
        if lineB_ccw_result1 == 0 and point_on_line(lineA[0], lineB):
            result = True
        if lineB_ccw_result2 == 0 and point_on_line(lineA[1], lineB):
            result = True

    return result

def polygon_intersection(polygonA, polygonB):
    
    result = False
    
    for indexA in range(len(polygonA)):
        
        if indexA == len(polygonA) - 1:
            lineA = [polygonA[indexA], polygonA[0]]
        else:
            lineA = [polygonA[indexA], polygonA[indexA+1]]
            
        for indexB in range(len(polygonB)):
            
            if indexB == len(polygonB) - 1:
                lineB = [polygonB[indexB], polygonB[0]]
            else:
                lineB = [polygonB[indexB], polygonB[indexB+1]]
        
            if line_intersection(lineA, lineB):
                result = True
                break
        
    return result

def point_in_polygon(point, polygon):
    
    result = True
    for index in range(len(polygon)):
        
        if index == len(polygon) - 1:
            ccw_result = ccw(polygon[-1], polygon[0], point)
            if ccw_result > 0 or (ccw_result == 0 and not point_on_line(point, [polygon[index], polygon[0]])):
                result = False
        else:
            ccw_result = ccw(polygon[index], polygon[index+1], point)
            if ccw_result > 0 or (ccw_result == 0 and not point_on_line(point, [polygon[index], polygon[index+1]])):
                result = False
                break
        
    return result
    
def line_in_polygon(line, polygon):
    
    result = True
    for point in line:
        if not point_in_polygon(point, polygon):
            result = False
            
    return result

def polygon_in_polygon(polygonA, polygonB):
    
    polygonA_in_polygonB = True
    for point in polygonA:
        if not point_in_polygon(point, polygonB):
            polygonA_in_polygonB = False
            break
    
    polygonB_in_polygonA = True
    for point in polygonB:
        if not point_in_polygon(point, polygonA):
            polygonB_in_polygonA = False
            break
    
    if polygonA_in_polygonB or polygonB_in_polygonA:
        return True
    else:
        return False


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    black_count, white_count = map(int, sys.stdin.readline().split())
    
    black_points = []
    for point in range(black_count):
        x, y = map(int, sys.stdin.readline().split())
        black_points.append((x, y))
    black_points.sort()
    
    white_points = []
    for point in range(white_count):
        x, y = map(int, sys.stdin.readline().split())
        white_points.append((x, y))
    white_points.sort()
        
    
    # 5. TO SOLVE THE PROBLEM
    
    black_convex_hull = convex_hull(black_points)
    white_convex_hull = convex_hull(white_points)
    
    if len(black_convex_hull) > len(white_convex_hull):
        black_convex_hull, white_convex_hull = white_convex_hull, black_convex_hull

    if len(black_convex_hull) == 1:
        
        if len(white_convex_hull) == 1:
            print("YES")
        elif len(white_convex_hull) == 2:
            if point_on_line(black_convex_hull[0], white_convex_hull):
                print("NO")
            else:
                print("YES")
        else:
            if point_in_polygon(black_convex_hull[0], white_convex_hull):
                print("NO")
            else:
                print("YES")
                
    elif len(black_convex_hull) == 2:
        
        if len(white_convex_hull) == 2:
            if line_intersection(black_convex_hull, white_convex_hull):
                print("NO")
            else:
                print("YES")
        else:
            if polygon_intersection(black_convex_hull, white_convex_hull) or line_in_polygon(black_convex_hull, white_convex_hull):
                print("NO")
            else:
                print("YES")
                
    else:
        
        if polygon_intersection(black_convex_hull, white_convex_hull) or polygon_in_polygon(black_convex_hull, white_convex_hull):
            print("NO")
        else:
            print("YES")