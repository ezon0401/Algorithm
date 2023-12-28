'''
BOJ 17435 - Composite Function and Queries (https://www.acmicpc.net/problem/17435)

There is a function f(x).
Given n and x, calculate f_n(x). 
'''

import sys


# 1. TO GET THE INPUT

num_count = int(sys.stdin.readline())
function = [0] + list(map(int, sys.stdin.readline().split()))


# 2. TO CREATE SPARSE TABLE 
# sparse_table[n][x] = f_2^x(n)

key = 23
sparse_table = [[-1 for exponent in range(key)] for num in range(num_count + 1)]

for num in range(1, num_count + 1):
    sparse_table[num][0] = function[num]

for exponent in range(1, key):
    for num in range(1, num_count + 1):
        if sparse_table[num][exponent-1] != -1:
            sparse_table[num][exponent] = sparse_table[sparse_table[num][exponent-1]][exponent-1]


# 3. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())
for query in range(query_count):
    composite, num = map(int, sys.stdin.readline().split())
    for exponent in range(key-1, -1, -1):
        if composite >= 2 ** exponent:
            num = sparse_table[num][exponent]
            composite -= 2 ** exponent
    print(num)