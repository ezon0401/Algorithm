'''
BOJ 11722 - Longest Decreasing Subsequence (https://www.acmicpc.net/problem/11722)

Given an array, print the length of the longest decreasing subsequence.
'''

import sys


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM - O(N^2) LIS DP

dp = [1 for index in range(arr_length)]

for now_index in range(arr_length):
    for before_index in range(now_index):
        if arr[now_index] < arr[before_index]:
            dp[now_index] = max(dp[before_index] + 1, dp[now_index])

print(max(dp))