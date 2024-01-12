'''
BOJ 23323 - Bull Tamagochi (https://www.acmicpc.net/problem/23323)

A bull has an initial HP of N and M foods.
Every morning, the bull can increase HP by x with x foods. Every night, HP decreases to half.
Determine the maximum number of days until the bull dies.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# The bull does not die unless there is no food.

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    life, food = map(int, sys.stdin.readline().split())
    
    count = 0
    while life != 0:
        life //= 2
        count += 1

    print(count + food)