'''
BOJ 17179 - Cake Cutting (https://www.acmicpc.net/problem/17179)

There is a roll cake of length L.
You can cut the roll cake X times among M given points.
Answer N queries: Given X, what is the maximum value of the length of the shortest piece?
'''

import sys


# 2. A FUNCTION TO CHECK WHETHER A GIVEN LENGTH IS POSSIBLE

def check(piece_length):
    
    now_cut = 0
    now_length = 0
            
    for index in range(1, len(points)):
        unit_length = points[index] - points[index-1]
        if now_length + unit_length < piece_length:
            now_length += unit_length
        else:
            now_cut += 1
            now_length = 0
    
    if now_cut > cut_count:
        return True
    elif now_cut == cut_count and now_length + cake_length - points[-1] >= piece_length:
        return True
    else:
        return False


# 1. TO GET THE INPUT

query_count, point_count, cake_length = map(int, sys.stdin.readline().split())

points = [0]
for point in range(point_count):
    points.append(int(sys.stdin.readline()))


# 3. TO SOLVE THE PROBLEM

for query in range(query_count):
    
    cut_count = int(sys.stdin.readline())
    
    left = 1
    right = 4000000
    
    while left + 1 < right:
        
        mid = (left + right) // 2
        
        if check(mid):
            left = mid
        else:
            right = mid
    
    print(left)