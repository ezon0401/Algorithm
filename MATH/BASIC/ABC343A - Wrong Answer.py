'''
ABC343A - Wrong Answer (https://atcoder.jp/contests/abc343/tasks/abc343_a)

Given A and B, print an integer between 0 and 9 that is not A + B.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

A, B = map(int, sys.stdin.readline().split())

if A == 0 and B == 0:
    print(1)
else:
    print(0)