'''
CF930B - Binary Path (https://codeforces.com/contest/1937/problem/B)

There is a 2 X n grid filled with 0s and 1s.
Suppose you can move only one cell right or downwards until you reach (2, n).
Find the lexicographically smallest string you can attain and the number of paths that yield the string.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    size = int(sys.stdin.readline())
    
    first_row = list(sys.stdin.readline().strip())
    second_row = list(sys.stdin.readline().strip())
    grid = [first_row, second_row]
    
    
    # 2. TO GET THE LEXICOGRAPHICALLY SMALLEST STRING
    
    now_row, now_col = 0, 0
    ans_string = [grid[0][0]]
    
    while True:
        
        if now_row == 1 and now_col == size - 1:
            
            break
        
        elif now_row == 1:
            
            ans_string += grid[now_row][now_col+1]
            now_col += 1
        
        elif now_col == size-1:
            
            ans_string += grid[now_row+1][now_col]
            now_row += 1
        
        else:
            
            right = grid[now_row][now_col+1]
            below = grid[now_row+1][now_col]
            
            if right == "1" and below == "0":
                ans_string.append(below)
                now_row += 1
            else:
                ans_string.append(right)
                now_col += 1
                
    print("".join(ans_string))
    
    
    # 3. TO GET THE NUMBER OF POSSIBLE PATHS
    
    first_row_best = 0
    for index in range(size):
        if ans_string[index] == grid[0][index]:
            first_row_best += 1
        else:
            break
        
    second_row_best = 0
    for index in range(-1, -size-1, -1):
        if ans_string[index] == grid[1][index]:
            second_row_best += 1
        else:
            break
    
    possible_downward_path = first_row_best + second_row_best - size
    print(possible_downward_path)