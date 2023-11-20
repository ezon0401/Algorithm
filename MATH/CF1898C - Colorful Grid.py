'''
CF1898C - Colorful Grid (https://codeforces.com/problemset/problem/1898/C)

Elena has a grid with N horizontal lines and M vertical lines.
Each line can be colored either red or blue.

Determine if it is possible for one to start from (1, 1) and end at (N, M) after walking K segments.
No two consecutive segments cannot have the same color.
If it exists, print any.  
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test_input in range(test_count):
    
    from_r = ["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B"]
    
    row_count, col_count, target = map(int, sys.stdin.readline().split())
    min_path = row_count + col_count - 2
    
    
    # 2. TO SOLVE THE PROBLEM
    # K should be larger than the length of a minimum path. 
    # By making a detour and a loop cell, it is possible to increase the length of a path by any even number.
    
    if target < min_path or (target - min_path) % 2 != 0:
        print("NO")
    else:
        
        print("YES")
        
        for horizontal_line in range(row_count):
            line = " ".join(from_r[:col_count-1])
            print(line)

        now = "R"
        if col_count % 2 == 0:
            now = "B"
        for vertical_line in range(row_count - 1):
            
            line = [now for index in range(col_count)]
            if vertical_line == 1:
                if now == "R":
                    line[-2] = "B"
                else:
                    line[-2] = "R"
            print(" ".join(line))
            
            if now == "R":
                now = "B"
            else:
                now = "R"
                