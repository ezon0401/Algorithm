'''
BOJ 17401 - Working Cells (https://www.acmicpc.net/problem/17401)

Graph transforms each second with a cycle of T seconds.
For every vertex pair (u, v), print the number of paths from u to v with a distance of D. 
'''

import sys


# 2. FUNCTIONS FOR MATRIX MULTIPLICATION

def matrix_multiplication(matrixA, matrixB):
    
    matrix = [[0 for vertexB in range(vertex_count)] for vertexA in range(vertex_count)]
    
    for i in range(vertex_count):
        for j in range(vertex_count):
            for k in range(vertex_count):
                matrix[i][j] += matrixA[i][k] * matrixB[k][j]
                matrix[i][j] %= mod

    return matrix

def matrix_pow(matrix, exponent):
    
    if exponent == 1:
        return matrix
    else:
        matrix_squared = matrix_multiplication(matrix, matrix)
        if exponent % 2 == 0:
            return matrix_pow(matrix_squared, exponent // 2)
        else:
            return matrix_multiplication(matrix_pow(matrix_squared, exponent // 2), matrix)


# 1. TO GET THE INPUT

mod = 10 ** 9 + 7

path = []

cycle, vertex_count, target_time = map(int, sys.stdin.readline().split())
for graph in range(cycle):
    
    matrix = [[0 for vertexB in range(vertex_count)] for vertexA in range(vertex_count)]
    
    edge_count = int(sys.stdin.readline())
    for edge in range(edge_count):
        start, end, count = map(int, sys.stdin.readline().split())
        matrix[start-1][end-1] = count
    
    path.append(matrix)


# 3. TO SOLVE THE PROBLEM
# If an adjacency matrix represents a graph, its K-th power represents the number of paths with a distance of K.

for time in range(1, cycle):
    path[time] = matrix_multiplication(path[time-1], path[time])

ans = None
if cycle >= target_time:
    ans = path[target_time-1]
else:
    ans = matrix_pow(path[-1], target_time // cycle)
    if target_time % cycle != 0:
        ans = matrix_multiplication(ans, path[target_time % cycle - 1])
        
for row in ans:
    print(" ".join(map(str, row)))