'''
BOJ 14490 - 100:10 (https://www.acmicpc.net/problem/14490)

Reduce a given ratio.
'''


import sys
from math import gcd


# 1. TO GET THE INPUT

ratio = sys.stdin.readline().strip()
numA, numB = map(int, ratio.split(":"))


# 2. TO SOLVE THE PROBLEM

GCD = gcd(numA, numB)

numA //= GCD
numB //= GCD

print(str(numA) + ":" + str(numB))