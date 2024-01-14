'''
BOJ 11012 - Egg (https://www.acmicpc.net/problem/11012)

There are N points on a plane. M rectangles are given.
Calculate the total sum of points covered by each rectangle.  
'''

import sys


# 3. A FUNCTION TO PROCESS QUERIES

def add(y):
    
    y += align
    while y != 0:
        seg_tree[y] += 1
        y >>= 1

def local_sum(start, end):
    
    start += align
    end += align
    
    result = 0
    while start <= end:
        if start % 2 == 1:
            result += seg_tree[start]
            start += 1
        if end % 2 == 0:
            result += seg_tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    return result


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    point_count, query_count = map(int, sys.stdin.readline().split())
    
    point = []
    for point_input in range(point_count):
        x, y = map(int, sys.stdin.readline().split())
        point.append((x, y))
    point.sort()
    
    # Let's denote the number of points from (0, 0) to (x, y) as point(x, y).
    # Then, the number of points in query (l, r, b, t) would be point(r, t) - point(r, b-1) - point(l-1, t) + point(l-1, b-1).
    query = []
    for query_num in range(query_count):
        left, right, bottom, top = map(int, sys.stdin.readline().split())
        query.append((right, top, True))
        query.append((right, bottom-1, False))
        query.append((left-1, top, False))
        query.append((left-1, bottom-1, True))
    query.sort()

    
    # 2. TO CONSTRUCT SEGMENT TREE
    
    align = 1 << 17
    seg_tree = [0 for index in range(1 << 18)]
    
    
    # 4. TO SOLVE THE PROBLEM
    
    point_index = 0
    
    ans = 0
    for x, y, plus in query:
        
        while point_index < point_count and point[point_index][0] <= x:
            point_x, point_y = point[point_index]
            add(point_y)
            point_index += 1
        
        result = local_sum(0, y)
        if plus:
            ans += result
        else:
            ans -= result
    
    print(ans)