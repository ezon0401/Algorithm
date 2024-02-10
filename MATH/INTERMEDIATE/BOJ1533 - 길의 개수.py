'''
BOJ 1533 - The Number of Paths (https://www.acmicpc.net/problem/1533)

There is a weighted adjacency matrix A. A[i][j] represents the length of a path from i to j.
Print the number of paths from u to v with a distance of X. 
'''

import sys


# 2. FUNCTIONS TO PROCESS QUERIES

def matrix_multiple(matrixA, matrixB):
    
    result = [[0 for end in range(5 * vertex_count)] for start in range(5 * vertex_count)]
    
    for i in range(5 * vertex_count):
        for j in range(5 * vertex_count):
            for k in range(5 * vertex_count):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
                result[i][j] %= mod
    
    return result

def matrix_pow(matrix, exponent):
    
    if exponent == 1:
        return matrix
    else:
        matrix_squared = matrix_multiple(matrix, matrix)
        if exponent % 2 == 0:
            return matrix_pow(matrix_squared, exponent // 2)
        else:
            return matrix_multiple(matrix_pow(matrix_squared, exponent // 2), matrix)



# 1. TO GET THE INPUT

mod = 10 ** 6 + 3

vertex_count, start_node, end_node, target_time = map(int, sys.stdin.readline().split())
start_node -= 1
end_node -= 1

graph = [[0 for end in range(5 * vertex_count)] for start in range(5 * vertex_count)]

for start in range(vertex_count):
    row = list(sys.stdin.readline().strip())
    row = list(map(int, row))
    for end in range(vertex_count):
        
        # To make a graph into unweighted adjacency matrix
        for offset in range(row[end]):
            if offset == row[end] - 1:
                graph[5*start+offset][5*end] = 1
            else:
                graph[5*start+offset][5*start+offset+1] = 1


# 3. TO SOLVE THE PROBLEM

graph = matrix_pow(graph, target_time)
print(graph[5*start_node][5*end_node])