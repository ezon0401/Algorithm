'''
ABC330B - Minimize Abs 1 (https://atcoder.jp/contests/abc330/tasks/abc330_b)

There is an integer sequence A of length N and integers L and R such that L <= R.
For each index, find the integer X that satisfies the following conditions.

(1) L <= X <= R
(2) For every integer Y such that L <= Y <= R, abs(X - A[i]) <= abs(Y - A[i])
'''

import sys


# 1. TO SOLVE THE PROBLEM

arr_length, min_num, max_num = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = []
for num in arr:
    if num < min_num:
        ans.append(min_num)
    elif num > max_num:
        ans.append(max_num)
    else:
        ans.append(num)

print(" ".join(map(str, ans)))