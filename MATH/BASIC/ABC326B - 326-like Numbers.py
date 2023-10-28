'''
ABC326B - 326-like Numbers (https://atcoder.jp/contests/abc326/tasks/abc326_b)

A 326-like number is a three-digit positive integer where the product of the hundreds and tens digits equals the one's digit.
Given an integer N, find the smallest 326-like number greater than or equal to N.
'''

import sys

# 1. TO SOLVE THE PROBLEM

N = int(sys.stdin.readline())

for num in range(N, 1000):
    num = str(num)
    digit_hundreds = int(num[0])
    digit_tens = int(num[1])
    digit_ones = int(num[2])
    if digit_hundreds * digit_tens == digit_ones:
        print(num)
        break
