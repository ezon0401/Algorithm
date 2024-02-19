'''
BOJ 1030 - Fractal Plane (https://www.acmicpc.net/problem/1030)

At time 0, a plane consists of one white square.
At each second, a plane is divided into N X N squares, and K X K squares at the center will be painted black.
Determine the result of the area (r1, c1) ~ (r2, c2) after S seconds.
'''

import sys


# 2. A FUNCTION TO RETURN THE COLOR OF (ROW, COL) AFTER S SECONDS

def color(row, col, r1, c1, r2, c2):
    
    size = (r2 - r1) // divide_size
    blank = (r2 - r1 - paint_size * size) // 2
    
    if r1 + blank <= row < r2 - blank and c1 + blank <= col < c2 - blank:
        
        return 1
    
    else:
        
        if size == 1:
            return 0
        else:
            for row_loc in range(r1, r2, size):
                for col_loc in range(c1, c2, size):
                    if row_loc <= row < row_loc + size and col_loc <= col < col_loc + size:
                        return color(row, col, row_loc, col_loc, row_loc + size, col_loc + size)

                

# 1. TO GET THE INPUT

time, divide_size, paint_size, r1, r2, c1, c2 = map(int, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM

if time == 0:
    
    print("0")
    
else:
    
    ans = [[0 for col in range(c2 - c1 + 1)] for row in range(r2 - r1 + 1)]

    for row in range(r2 - r1 + 1):
        for col in range(c2 - c1 + 1):
            ans[row][col] = color(row + r1, col + c1, 0, 0, divide_size ** time, divide_size ** time)

    for row in ans:
        print("".join(map(str, row)))