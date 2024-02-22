'''
BOJ 9934 - Complete Binary Tree (https://www.acmicpc.net/problem/9934)

Given a result of the in-order traversal of a complete binary tree, print vertices on each level.
'''

import sys


# 2. A FUNCTION TO SOLVE THE PROBLEM

def solve(start, end, level):
    
    mid = (start + end) // 2
    
    ans[level].append(str(inorder[mid]))
    if start != end:
        solve(start, mid-1, level+1)
        solve(mid+1, end, level+1)


# 1. TO GET THE INPUT

level_count = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))


# 3. TO SOLVE THE PROBLEM

ans = [[] for level in range(level_count)]

solve(0, len(inorder) - 1, 0)

for level in ans:
    print(" ".join(level))