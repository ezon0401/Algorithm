'''
BOJ 31403 - A + B - C (https://www.acmicpc.net/problem/31403)

Print the result of A + B - C in JavaScript when A, B, and C are integers and strings.
'''

import sys

# 1. TO GET THE INPUT

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM

print(A + B - C)
print(int(str(A) + str(B)) - C)