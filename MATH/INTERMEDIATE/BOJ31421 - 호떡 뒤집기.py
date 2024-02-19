'''
BOJ 31421 - Pancake Flip (https://www.acmicpc.net/problem/31421)

There are N pancakes in row A. Initially, the white side is on top, and the brown side is on the bottom for every pancake.
A chef can execute the following operations at most N times:

(1) Choose index x such that A[x] equals A[x+1].
(2) If A[x] equals white, flip A[0] ~ A[x]. Otherwise, flip A[x+1] ~ A[N-1].

Given a target array, determine whether it is possible to construct the array.
If possible, print any possible way.
'''

import sys


# 1. TO GET THE INPUT

pancake_count = int(sys.stdin.readline())
target = list(sys.stdin.readline().strip())


# 2. STRING COMPRESSION FOR IMPOSSIBLE CASES

compressed = target[0]
before = target[0]

for index in range(pancake_count):
    if target[index] != before:
        compressed += target[index]
        if len(compressed) == 3:
            break
        before = target[index]


# 3. TO SOLVE THE PROBLEM
# Key observation : The chef must execute an operation on A[x] if target[x] != target[x+1].

if (compressed == "WB") or (compressed == "B"):
    print(-1)
    
else:
    
    ans = []
    for index in range(pancake_count-1):
        if target[index] != target[index+1]:
            ans.append(index+1)
    
    print(len(ans))
    if (target[0] == "W" and len(ans) % 2 == 1) or (target[0] == "B" and len(ans) % 2 == 0):
        print(ans.pop())
    for index in range(len(ans)):
        print(ans[index])