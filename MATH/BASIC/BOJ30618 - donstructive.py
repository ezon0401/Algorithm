'''
BOJ 30618 - donstructive (https://www.acmicpc.net/problem/30618)

The score of a permutation P is the sum of sum(S) for all consecutive subsequences S for P.
What is the permutation P with maximum score when the length N is given?
'''

import sys


# 1. TO SOLVE THE PROBLEM
# The closer a number is to the middle, the more influential the number is to the score.

permutation_length = int(sys.stdin.readline())

ans = []

odd_num = 1
while odd_num <= permutation_length:
    ans.append(odd_num)
    odd_num += 2

even_num = permutation_length
if even_num % 2 == 1:
    even_num -= 1
while even_num > 0:
    ans.append(even_num)
    even_num -= 2

print(" ".join(map(str, ans)))