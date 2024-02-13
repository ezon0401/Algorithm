'''
BOJ 1535 - Thanks (https://www.acmicpc.net/problem/1535)

Se-joon wants to thank some people.
When he thanks i-th person, he loses health by L[i] and earns happiness by J[i].
The initial health of Se-joon is 100 and he can only thank each person once.
Determine the maximum happiness he can earn.
'''


import sys


# 1. TO GET THE INPUT

person_count = int(sys.stdin.readline())
weight = [0] + list(map(int, sys.stdin.readline().split()))
value = [0] + list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM (KNAPSACK DP)

dp = [[0 for max_weight in range(100)] for person in range(person_count + 1)]

for person in range(1, person_count + 1):
    for max_weight in range(100):
        if weight[person] > max_weight:
            dp[person][max_weight] = dp[person-1][max_weight]
        else:
            dp[person][max_weight] = max(dp[person-1][max_weight], dp[person-1][max_weight - weight[person]] + value[person])

print(dp[-1][-1])