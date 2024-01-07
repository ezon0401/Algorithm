'''
ABC332B - Tetrahedral Number (https://atcoder.jp/contests/abc335/tasks/abc335_b)

Print all (x, y, z) triples such that x + y + z <= N in ascending lexicographical order. 
'''


import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

goal = int(sys.stdin.readline())

case = []

for x in range(goal + 1):
    for y in range(goal + 1):
        for z in range(goal + 1):
            if x + y + z <= goal:
                case.append((x, y, z))
case.sort()

for x, y, z in case:
    print(x, y, z)