'''
BOJ 11382 - Price of Sweet Cone (https://www.acmicpc.net/problem/30030)

Given a price with 10% tax, calculate a price without tax.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

price_with_tax = int(sys.stdin.readline())

print(price_with_tax // 11 * 10)