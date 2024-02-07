'''
BOJ 30804 - Fruit Tanghulu (https://www.acmicpc.net/problem/30804)

Given an array, print the length of the longest substring, which consists of two or fewer numbers.
'''

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
tanghulu = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM (TWO POINTER)

ans = 1

fruit_count = [0 for index in range(10)]
fruit_count[tanghulu[0]] = 1
fruit_kind = 1

left = 0
right = 0

while True:
    
    if fruit_kind <= 2:
        
        ans = max(ans, right - left + 1)
        
        right += 1
        if right == length:
            break
        fruit_count[tanghulu[right]] += 1
        if fruit_count[tanghulu[right]] == 1:
            fruit_kind += 1
    
    else:
        
        fruit_count[tanghulu[left]] -= 1
        if fruit_count[tanghulu[left]] == 0:
            fruit_kind -= 1
        left += 1
    
print(ans)