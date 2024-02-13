'''
BOJ 9084 - Coin (https://www.acmicpc.net/problem/9084)

Given N kinds of coins and their values, print the number of ways to make the value of M. 
'''


import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    coin_count = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    
    target_price = int(sys.stdin.readline())
    
    
    # 2. TO SOLVE THE PROBLEM (DYNAMIC PROGRAMMING)
    
    dp = [0 for price in range(target_price + 1)]
    dp[0] = 1
    
    for coin in coins:
        for price in range(target_price + 1):
            if price - coin >= 0:
                dp[price] += dp[price - coin]
    
    print(dp[-1])