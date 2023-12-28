'''
BOJ 11438 - LCA 2 (https://www.acmicpc.net/problem/11438)

Given a tree with weighted edges, answer queries: What is the longest and shortest edge in the path from node X to node Y?
'''

import sys
sys.setrecursionlimit(10 ** 5)


# 3. A FUNCTION TO SET NODE DEPTHS

def set_depth(node, node_depth):
    
    visited[node] = 1
    depth[node] = node_depth
    
    for next_node, dist in graph[node]:
        if visited[next_node] == -1:
            parent[next_node][0] = node
            dp[next_node][0] = [dist, dist]
            set_depth(next_node, node_depth + 1)


# 4. A FUNCTION TO FILL TABLES

def set_tables():
    
    for exponent in range(1, key):
        for node in range(1, city_count + 1):
            
            parent[node][exponent] = parent[parent[node][exponent-1]][exponent-1]
            if depth[node] >= (1 << exponent):
                dp[node][exponent][0] = min(dp[node][exponent-1][0], dp[parent[node][exponent-1]][exponent-1][0])
                dp[node][exponent][1] = max(dp[node][exponent-1][1], dp[parent[node][exponent-1]][exponent-1][1])
                

# 5. A FUNCTION TO SOLVE THE PROBLEM : LCA + DP

def solve(nodeA, nodeB):
    
    MIN = inf
    MAX = -inf
    
    if depth[nodeA] > depth[nodeB]:
        nodeA, nodeB = nodeB, nodeA
    
    for exponent in range(key-1, -1, -1):
        if depth[nodeB] - depth[nodeA] >= (1 << exponent):
            MIN = min(MIN, dp[nodeB][exponent][0])
            MAX = max(MAX, dp[nodeB][exponent][1])
            nodeB = parent[nodeB][exponent]
    
    if nodeA == nodeB:
        print(MIN, MAX)
        return
    
    for exponent in range(key-1, -1, -1):
        if parent[nodeA][exponent] != parent[nodeB][exponent]:
            MIN = min(MIN, dp[nodeA][exponent][0], dp[nodeB][exponent][0])
            MAX = max(MAX, dp[nodeA][exponent][1], dp[nodeB][exponent][1])
            nodeA = parent[nodeA][exponent]
            nodeB = parent[nodeB][exponent]
    
    MIN = min(MIN, dp[nodeA][0][0], dp[nodeB][0][0])
    MAX = max(MAX, dp[nodeA][0][1], dp[nodeB][0][1])
    print(MIN, MAX)
    return


# 1. TO GET THE INPUT

city_count = int(sys.stdin.readline())

graph = {}
for city in range(1, city_count + 1):
    graph[city] = []

for edge in range(city_count - 1):
    cityA, cityB, dist = map(int, sys.stdin.readline().split())
    graph[cityA].append((cityB, dist))
    graph[cityB].append((cityA, dist))


# 2. TO CONSTRUCT TABLES

key = 17
inf = float('inf')

depth = [-1 for city in range(city_count + 1)]
visited = [-1 for city in range(city_count + 1)]

parent = [[-1 for exponent in range(key)] for city in range(city_count + 1)]
dp = [[[inf, -inf] for exponent in range(key)] for city in range(city_count + 1)]


# 6. TO SOLVE THE PROBLEM

set_depth(1, 0)
set_tables()

query_count = int(sys.stdin.readline())
for query in range(query_count):
    cityA, cityB = map(int, sys.stdin.readline().split())
    solve(cityA, cityB)
