'''
CF930A - Shuffle Party (https://codeforces.com/contest/1937/problem/A)

There is an array A = [1, 2, ..., n].
For the largest divisor d of k, which is not equal to k itself, the operation swap(k) swaps the elements A[k] and A[d].
Suppose performing a swap(i) for i = 2, 3, ..., n, find the position of 1 in the resulting array.
'''

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM
# The path of 1 is following: 1 > 2 > 4 > ...

test_count = int(sys.stdin.readline())
for test in range(test_count):

    num = int(sys.stdin.readline())

    ans = 1
    while ans * 2 <= num:
        ans *= 2

    print(ans)