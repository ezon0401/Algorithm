'''
BOJ 15423 - Canonical Coin System (https://www.acmicpc.net/problem/15423)

A coin system is canonical if the greedy algorithm provides the smallest number of coins required to dispense x for all x.
Determine if a coin system is canonical or not.
If a coin system is non-canonical, the smallest counterexample is less than the sum of the two largest denominations.
'''


import sys
from collections import deque


# 2. A FUNCTION TO SOLVE THE SMALLEST NUMBER OF COINS PROBLEM BY GREEDY ALGORITHM

def greedy(value):
    
    count = 0
    for index in range(coin_count-1, -1, -1):
        if coins[index] <= value:
            count += value // coins[index]
            value %= coins[index]
    return count


# 1. TO GET THE INPUT

coin_count = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))


# 3. TO SOLVE THE SMALLEST NUMBER OF COINS PROBLEM BY DP

dp = [0 for index in range(coins[-1] + coins[-2] + 1)]
for value in range(1, coins[-1] + coins[-2] + 1):
    least = float('inf')
    for coin in coins:
        if value < coin:
            break
        else:
            if dp[value - coin] < least:
                least = dp[value - coin]
    dp[value] = least + 1


# 4. TO SOLVE THE PROBLEM

canonical = True
for value in range(1, coins[-1] + coins[-2] + 1):
    if greedy(value) > dp[value]:
        canonical = False
        break

if canonical:
    print("canonical")
else:
    print("non-canonical")