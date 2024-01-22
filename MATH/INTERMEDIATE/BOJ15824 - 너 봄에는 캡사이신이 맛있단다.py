'''
BOJ 15824 - You know, Capsaicin tastes better at spring (https://www.acmicpc.net/problem/15824)

There is an array A of length N.
When f(i, j) = max(A[i:j+1]) - min(A[i:j+1]), calculate the sum of f(i, j) for every pair (i, j).
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

mod = 10 ** 9 + 7

menu_count = int(sys.stdin.readline())
menu = list(map(int, sys.stdin.readline().split()))
menu.sort()


# 2. TO SOLVE THE PROBLEM
# Following is the simplified version of the code below.

'''
ans = 0

for i in range(menu_count):
    for j in range(i+1, menu_count):
        count = pow(menu[j] - menu[i], 1, mod) * pow(2, j-i-1, mod)
        ans = ((ans % mod) + (count % mod)) % mod
'''

ans = 0

count = pow(2, menu_count-1, mod) - 1
exponent_two = deque([pow(2, index, mod) for index in range(menu_count-1)])

for index in range(menu_count // 2):
    
    spiciness = menu[-index-1] - menu[index]
    ans = ((ans % mod) + ((spiciness % mod) * (count % mod) % mod)) % mod
    
    if len(exponent_two) >= 2:
        count = ((count % mod) - ((exponent_two.popleft() + exponent_two.pop()) % mod)) % mod
    
print(ans)    