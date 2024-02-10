'''
BOJ 24954 - Potion Purchase (https://www.acmicpc.net/problem/24954)

N potions and their prices are given.
There is a discount event going on so that customers can get discounted prices of some potions if they buy a potion.
Given the details of the discount event, determine the minimum cost to buy all potions. 
'''


import sys
from itertools import permutations


# 1. TO GET THE INPUT

potion_count = int(sys.stdin.readline())
price = [0] + list(map(int, sys.stdin.readline().split()))

discount = {}
for potion in range(1, potion_count+1):
    discount[potion] = []

for potion in range(1, potion_count+1):
    info_count = int(sys.stdin.readline())
    for info in range(info_count):
        potion_num, discount_price = map(int, sys.stdin.readline().split())
        discount[potion].append((potion_num, discount_price))


# 2. TO SOLVE THE PROBLEM

ans = float('inf')

for permutation in permutations(range(1, potion_count+1), potion_count):
    
    now_price = price[:]
    cost = 0
    
    for potion in permutation:
        cost += now_price[potion]
        for potion_num, discount_price in discount[potion]:
            now_price[potion_num] = max(1, now_price[potion_num] - discount_price)
    
    ans = min(ans, cost)

print(ans)