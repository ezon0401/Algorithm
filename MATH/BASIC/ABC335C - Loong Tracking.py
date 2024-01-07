'''
ABC332C - Loong Tracking (https://atcoder.jp/contests/abc335/tasks/abc335_c)

The dragon consists of N parts. Initially, part i is located at the coordinates (i, 0).
Process Q queries. There are two following query types:

(1) Query 1: Move the head by 1 in a direction.
(2) Query 2: Find the coordinates of part p. 
'''


import sys

# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

part_count, query_count = map(int, sys.stdin.readline().split())

dragon = [(index, 0) for index in range(part_count, 0, -1)]

for query in range(query_count):
    
    query_type, key = sys.stdin.readline().strip().split()
    
    if query_type == "1":
        
        x, y = dragon[-1]
        if key == "U":
            dragon.append((x, y+1))
        elif key == "D":
            dragon.append((x, y-1))
        elif key == "L":
            dragon.append((x-1, y))
        else:
            dragon.append((x+1, y))
    
    else:
        
        key = int(key)
        x, y = dragon[-key]
        print(x, y)