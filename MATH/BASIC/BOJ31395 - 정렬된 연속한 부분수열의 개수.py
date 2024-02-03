'''
BOJ 31395 - Number of Sorted Sub-array (https://www.acmicpc.net/problem/31395)

Given an array A, print the number of pairs (i, j) such that A[i:j+1] is sorted.
'''

import sys


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = 0

row = 1
for index in range(1, arr_length):
    if arr[index] > arr[index-1]:
        row += 1
    else:
        ans += row * (row + 1) // 2
        row = 1

ans += row * (row + 1) // 2

print(ans)