'''
ABC343B - Adjacency Matrix (https://atcoder.jp/contests/abc343/tasks/abc343_b)

Given an adjacency matrix A, print j in the i-th line if A[i][j] == 1.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

size = int(sys.stdin.readline())

matrix = []
for row_input in range(size):
    row = list(map(int, sys.stdin.readline().split()))
    matrix.append(row)

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 1:
            print(col+1, end = ' ')
    print()