'''
BOJ 3679 - Simple Polygon (https://www.acmicpc.net/problem/3679)

Given N points, print a sequence of which points constitute a simple polygon.
'''

import sys


# 2. A FUNCTION TO GET SLOPE

def get_slope(point1, point2):
    
    x1, y1, num1 = point1
    x2, y2, num2 = point2
    
    if x1 - x2 == 0:
        return float('inf')
    else:
        return (y1 - y2) / (x1 - x2)
    

# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    input_line = list(map(int, sys.stdin.readline().strip().split()))
    
    points = []
    for index in range(1, len(input_line), 2):
        x, y = input_line[index], input_line[index+1]
        points.append((x, y, index // 2))
    points.sort(reverse=True)
    
    
    # 3. SORTING BY ANGLES
    
    start = points.pop()
    points.sort(key = lambda x : (get_slope(x, start), x[0], x[1]))
    
    # If the last two points and the start point are on the same line, the last points should come in reversed order. 
    
    exception = []
    while get_slope(points[-2], points[-1]) == get_slope(points[-1], start):
        exception.append(points.pop())
    exception.append(points.pop())
    exception.append(start)
    
    points += exception
    for x, y, num in points:
        print(num, end = ' ')
    print()