'''
BOJ 19951 - Tae-sang in Training Camp (https://www.acmicpc.net/problem/19951)

There is an array A. M queries are given: Add k to A[a:b+1].
Print the array after processing all M queries.
'''

import sys


# 1. TO GET THE INPUT

ground_length, query_count = map(int, sys.stdin.readline().split())
ground = list(map(int, sys.stdin.readline().split()))


# 2. TO GET THE QUERIES

query_sum = [0 for index in range(ground_length+1)]

for query in range(query_count):
    start, end, change = map(int, sys.stdin.readline().split())
    query_sum[start-1] += change
    query_sum[end] -= change


# 3. TO SOLVE THE PROBLEM (IMOS)
# The prefix sum of query_sum equals the change for each element. 

for index in range(1, ground_length):
    query_sum[index] += query_sum[index-1]

for index in range(ground_length):
    ground[index] += query_sum[index]
    print(ground[index], end = ' ')
