'''
BOJ 9741 - Interior Lattice Points (https://www.acmicpc.net/problem/9741)

Three coordinates are given to describe a triangle with a non-zero area.
Print the number of interior lattice points of the triangle.
'''

import sys


# 2. CCW

def ccw(x1, y1, x2, y2, x3, y3):
    
    direction = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    
    if direction > 0:
        direction = 1
    elif direction < 0:
        direction = -1
    else:
        direction = 0
    
    return direction


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().split())
    
    # 2. TO SOLVE THE PROBLEM
    # The point (x, y) is an interior lattice point if the direction of the point in regard to each segment is the same.
    
    ans = 0
    
    if ccw(x1, y1, x2, y2, x3, y3) != 0:
        for x_val in range(101):
            for y_val in range(101):
                ccw1 = ccw(x1, y1, x2, y2, x_val, y_val)
                ccw2 = ccw(x2, y2, x3, y3, x_val, y_val)
                ccw3 = ccw(x3, y3, x1, y1, x_val, y_val)
                if ccw1 == ccw2 == ccw3:
                    ans += 1
    
    print(ans)        