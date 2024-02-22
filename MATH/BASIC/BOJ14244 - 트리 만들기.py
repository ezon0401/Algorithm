'''
BOJ 14244 - Tree Construction (https://www.acmicpc.net/problem/14244)

Construct a tree with N nodes, including M leaf nodes.
'''

import sys


# 1. TO GET THE INPUT

node_count, leaf_count = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

# A straight line is a tree with 2 leaf nodes.

for node in range(node_count - leaf_count + 1):
    print(node, node+1)
for node in range(node_count - leaf_count + 2, node_count):
    print(1, node)