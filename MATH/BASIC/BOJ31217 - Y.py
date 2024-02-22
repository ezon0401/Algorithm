'''
BOJ 31217 - Y (https://www.acmicpc.net/problem/31217)

Given a graph, print the number of Y in the graph.
'''

import sys


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

degree = [0 for node in range(node_count + 1)]

for edge in range(edge_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    degree[nodeA] += 1
    degree[nodeB] += 1


# 2. TO SOLVE THE PROBLEM

mod = 10 ** 9 + 7

ans = 0
for node in range(1, node_count+1):
    if degree[node] >= 3:
        ans += degree[node] * (degree[node]-1) * (degree[node]-2) // 6
        ans %= mod

print(ans)