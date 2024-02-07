'''
BOJ 25826 - 2D Array Multiple Updates Single Sum (https://www.acmicpc.net/problem/25826)

There is a 2D array A. M queries are given: Add k to A[i1:i2+1][j1:j2+1].
Calculate the sum of a given sub-array after processing all M queries.
'''

import sys


# 1. TO GET THE INPUT

grid_size, query_count = map(int, sys.stdin.readline().split())

grid = []
for row_input in range(grid_size):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 2. TO SOLVE THE PROBLEM (IMOS)

query_sum = [[0 for j in range(grid_size+1)] for i in range(grid_size+1)]

for query_input in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    if query[0] == 1:
        
        query_type, i1, j1, i2, j2, change = query
        
        query_sum[i1][j1] += change
        query_sum[i1][j2+1] -= change
        query_sum[i2+1][j1] -= change
        query_sum[i2+1][j2+1] += change
    
    else:
        
        query_type, i1, j1, i2, j2 = query
        
        for i in range(grid_size):
            for j in range(1, grid_size):
                query_sum[i][j] += query_sum[i][j-1]
        
        for j in range(grid_size):
            for i in range(1, grid_size):
                query_sum[i][j] += query_sum[i-1][j]
                
        ans = 0
        for i in range(i1, i2+1):
            for j in range(j1, j2+1):
                ans += grid[i][j] + query_sum[i][j]
        
        print(ans)