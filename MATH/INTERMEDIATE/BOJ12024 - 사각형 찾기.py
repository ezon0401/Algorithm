'''
BOJ 12024 - Find a square (https://www.acmicpc.net/problem/12024)

Given a graph, print the number of squares.
'''

import sys


# 2. A FUNCTION FOR MATRIX MULTIPLICATION

def matrix_square(matrix):
    
    result = [[0 for node in range(node_count)] for node in range(node_count)] 
    
    for i in range(node_count):
        for j in range(node_count):
            for k in range(node_count):
                result[i][j] += matrix[i][k] * matrix[k][j]
    
    return result


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

matrix = []
for node in range(node_count):
    adjacency = list(map(int, sys.stdin.readline().split()))
    matrix.append(adjacency)


# 3. TO SOLVE THE PROBLEM

squared_matrix = matrix_square(matrix)

ans = 0

for i in range(node_count):
    for j in range(node_count):
        if i != j:
            ans += squared_matrix[i][j] * squared_matrix[j][i]
            for k in range(node_count):
                ans -= matrix[i][k] * matrix[k][j] * matrix[j][k] * matrix[k][i]

print(ans)