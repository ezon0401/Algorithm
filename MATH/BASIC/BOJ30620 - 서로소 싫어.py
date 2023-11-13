'''
BOJ 30620 - I hate co-prime (https://www.acmicpc.net/problem/30620)

There are two numbers: x and y.
In each operation, you can choose the integer z such that x and z are co-prime and either add it to or subtract it from x.
Convert x to y within two operations.
'''

import sys


# 1. TO SOLVE THE PROBLEM
# Convert x to x * y, then y.

x, y = map(int, sys.stdin.readline().split())

if x == y:
    print(0)
else:
    print(2)
    print(x * y - x)
    print(y - x * y)