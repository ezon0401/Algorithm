'''
BOJ 29865 - Move Knight Twice (https://www.acmicpc.net/problem/29865)

The initial position of a knight is given.
Print all possible positions of the knight after two moves.
'''

import sys


# 2. A FUNCTION TO MOVE THE KNIGHT

def move(before):
    
    direction_y = [2, 2, 1, 1, -1, -1, -2, -2]
    direction_x = [1, -1, 2, -2, 2, -2, 1, -1]    
    
    after = set([])
    
    for y, x in before:
        for index in range(8):
            new_y = y + direction_y[index]
            new_x = x + direction_x[index]
            if 1 <= new_y <= 8 and 1 <= new_x <= 8:
                after.add((new_y, new_x))
    
    return list(after)
    

# 1. TO GET THE INPUT

start = sys.stdin.readline().strip()


# 3. TO SOLVE THE PROBLEM

not_moved = [(ord(start[0]) - 96, int(start[1]))]

moved_once = move(not_moved)
moved_twice = move(moved_once)

for y, x in moved_twice:
    print(chr(y + 96) + str(x))