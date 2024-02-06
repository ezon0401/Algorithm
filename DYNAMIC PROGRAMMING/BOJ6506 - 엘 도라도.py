'''
BOJ 6506 - El Dorado (https://www.acmicpc.net/problem/6506)

Given an array, print the number of increasing subsequences with length L.
'''

import sys


# 1. TO GET THE INPUT

while True:
    
    arr_length, target_length = map(int, sys.stdin.readline().split())
    if arr_length == 0 and target_length == 0:
        break
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO CONSTRUCT A GRAPH
    
    graph = {}
    for index in range(arr_length):
        graph[index] = []
    
    for i in range(arr_length):
        for j in range(arr_length):
            if arr[i] < arr[j]:
                graph[j].append(i)
    
    
    # 3. TO SOLVE THE PROBLEM (DYNAMIC PROGRAMMING)
    # dp[i][j] = The number of increasing subsequences of which arr[i] is a j-th number
    
    dp = [[0 for len in range(target_length)] for index in range(arr_length)]
    dp[0][0] = 1
    
    for index in range(1, arr_length):
        dp[index][0] = 1
        for smaller_index in graph[index]:
            for len in range(1, target_length):
                dp[index][len] += dp[smaller_index][len-1]
    
    ans = 0
    for index in range(arr_length):
        ans += dp[index][target_length-1]
    print(ans)