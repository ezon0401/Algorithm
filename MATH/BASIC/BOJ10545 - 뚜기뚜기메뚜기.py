'''
BOJ 10545 - Hop, Hop, Grasshopper (https://www.acmicpc.net/problem/10545)

Cellphone keys are malfunctioning.
When you press a key, it works as if you pressed another key.
Given how keys work, print how to type a given string. 
'''

import sys


# 1. TO GET THE INPUT

right_to_wrong = [0] + list(map(int, sys.stdin.readline().split()))
target_word = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

keys = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

ans = ""

before_key = -1

for target_char in target_word:
    
    for key in range(10):
        if target_char in keys[key]:
            if before_key == key:
                ans += "#"
            ans += str(right_to_wrong.index(key)) * (keys[key].index(target_char) + 1)
            before_key = key

print(ans)