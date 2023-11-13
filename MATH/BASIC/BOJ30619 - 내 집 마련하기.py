'''
BOJ 30619 - House Ownership (https://www.acmicpc.net/problem/30619)

If a person Y lives in a house X, he will get a tax reduction of XY.
Answer queries: How can we maximize the amount of tax reduction by re-arranging people L ~ R?
'''

import sys


# 1. TO SOLVE THE PROBLEM
# Idea is simple. It is always better to put a person with greater number at a house with greater number.

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

query_count = int(sys.stdin.readline())

for query_input in range(query_count):
    
    left, right = map(int, sys.stdin.readline().split())
    
    arr_copy = arr[:]
    now = left
    for index in range(arr_length):
        if left <= arr_copy[index] <= right:
            arr_copy[index] = now
            now += 1
    
    print(" ".join(map(str, arr_copy)))