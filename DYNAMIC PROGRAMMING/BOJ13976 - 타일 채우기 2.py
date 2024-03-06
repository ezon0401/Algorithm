'''
BOJ 13976 - Tile (https://www.acmicpc.net/problem/13976)

Print the number of cases to fill 3 X N space with 1 X 2 and 2 X 1 tiles. 
'''

import sys


# 2. MATRIX EXPONENTIATION

def matrix_multiplication(matrixA, matrixB):
    
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
                result[i][j] %= mod
    
    return result

def matrix_power(matrix, exp):
    
    if exp == 1:
        return matrix
    else:
        matrix_squared = matrix_multiplication(matrix, matrix)
        if exp % 2 == 0:
            return matrix_power(matrix_squared, exp // 2)
        else:
            return matrix_multiplication(matrix_power(matrix_squared, exp // 2), matrix)


# 1. TO GET THE INPUT

mod = 10 ** 9 + 7
length = int(sys.stdin.readline())


# 3. TO SOLVE THE PROBLEM
# dp[N] = 3 * dp[N-2] + 2 * (dp[N-4] + dp[N-6] + ... + dp[0])
# It is possible to optimize the program with matrix [[1, 1], [2, 3]].

if length % 2 == 1:
    print(0)
else:
    dp_matrix = [[1, 1], [2, 3]]
    dp_matrix = matrix_power(dp_matrix, length // 2)
    print(dp_matrix[1][1])