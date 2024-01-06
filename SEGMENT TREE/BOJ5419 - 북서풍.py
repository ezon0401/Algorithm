'''
BOJ 5419 - Northwester (https://www.acmicpc.net/problem/5419)

Island B is reachable from island A if x_A <= x_B and y_A >= y_B.
Given the coordinates of islands, determine the number of pairs (A, B) such that island B is reachable from island A.
'''

import sys


# 3. FUNCTIONS TO COUNT A NUMBER OF POSSIBLE PAIRS AND DELETE THE COORDINATE

def possible_pair(coordinate):
    
    x, y = coordinate
    
    start = alignment
    end = alignment + y_convert[y]
    
    pair_count = 0
    while start <= end:
        if start % 2 == 1:
            pair_count += seg_tree[start]
            start += 1
        if end % 2 == 0:
            pair_count += seg_tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    
    return pair_count - 1

def delete(coordinate):
    
    x, y = coordinate
    y = alignment + y_convert[y]
    while y != 0:
        seg_tree[y] -= 1
        y >>= 1


# 1. TO GET THE INPUT
# Coordinate compression to reduce complexity. 

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    islands = []
    
    y_coordinate = set()
    y_convert = {}
    
    island_count = int(sys.stdin.readline())
    for island in range(island_count):
        x, y = map(int, sys.stdin.readline().split())
        y_coordinate.add(y)
        islands.append((x, y))
        
    islands.sort(key = lambda coordinate : (-coordinate[0], coordinate[1]))
    
    y_coordinate = list(y_coordinate)
    y_coordinate.sort()
    now_num = 1
    for y in y_coordinate:
        y_convert[y] = now_num
        now_num += 1
    

    # 2. TO CONSTRUCT SEGMENT TREE
    # Segment tree implicitly stores the number of islands of which y_coordinate is smaller or equal to. 
    
    seg_tree = [0 for index in range(1 << 18)]
    alignment = (1 << 17) - 1
    for x, y in islands:
        seg_tree[alignment + y_convert[y]] += 1
    for index in range(alignment, 0, -1):
        seg_tree[index] = seg_tree[index << 1] + seg_tree[index << 1 | 1]
        
        
    # 4. TO SOLVE THE PROBLEM
    
    ans = 0
    while islands:
        island = islands.pop()
        ans += possible_pair(island)
        delete(island)
    print(ans)