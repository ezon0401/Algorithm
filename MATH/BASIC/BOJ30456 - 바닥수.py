'''
BOJ 30456 - Ground Number (https://www.acmicpc.net/problem/30456)

Given a number N, one can repeatedly change the number into its product of digits until it becomes a single digit.
The single-digit number is called the ground number.
Given a ground number and the number of digits of N, print one possible N.
'''

import sys

# 1. TO SOLVE THE PROBLEM
# The ground number of 1111111N is always N.

ground_num, digit_count = map(int, sys.stdin.readline().split())

print("1" * (digit_count - 1) + str(ground_num))