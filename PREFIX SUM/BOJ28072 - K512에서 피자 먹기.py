'''
BOJ 28072 - Eating Pizza at K512 (https://www.acmicpc.net/problem/28072)

There is a pizza sliced into N pieces. 
Each piece one eats should be a connected part, and its weight must be a multiple of K.
Given the weights of pizza slices, print the maximum number who can eat pizza.
'''

import sys


# 1. TO GET THE INPUT

piece_count, target = map(int, sys.stdin.readline().split())
pieces = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# Since the weight of a whole pizza is a multiple of K, the maximum number who can eat pizza equals the maximum count a number repeats.

count = [0 for num in range(target)]
prefix_sum = []

for piece in pieces:
    if len(prefix_sum) == 0:
        prefix_sum.append(piece % target)
    else:
        prefix_sum.append((piece + prefix_sum[-1]) % target)
    count[prefix_sum[-1]] += 1

print(max(count))