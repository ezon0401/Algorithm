'''
BOJ 13211 - Tree and Queries 2 (https://www.acmicpc.net/problem/13211)

Given a tree with weighted edges, answer two queries.
(1) Print the cost from vertex u to vertex v.
(2) Print the k-th vertex of the path from vertex u to vertex v.
'''

import sys
sys.setrecursionlimit(500000)


# 3. A FUNCTION TO SET NODE DEPTHS

def set_depth(node, node_depth):
    
    depth[node] = node_depth
    visited[node] = 1
    for next_node, weight in graph[node]:
        if visited[next_node] == -1:
            parent[next_node][0] = node
            cost[next_node][0] = weight
            set_depth(next_node, node_depth + 1)


# 4. A FUNCTION TO SET TABLES

def set_tables():
    
    for exponent in range(1, key):
        for node in range(1, node_count + 1):
            if depth[node] >= (1 << exponent):
                parent[node][exponent] = parent[parent[node][exponent-1]][exponent-1]
                cost[node][exponent] = cost[node][exponent-1] + cost[parent[node][exponent-1]][exponent-1]


# 5. A FUNCTION TO ANSWER QUERIES

def lca(nodeA, nodeB):
    
    if depth[nodeA] > depth[nodeB]:
        nodeA, nodeB = nodeB, nodeA
    
    for exponent in range(key-1, -1, -1):
        if depth[nodeB] - depth[nodeA] >= (1 << exponent):
            nodeB = parent[nodeB][exponent]
    
    if nodeA == nodeB:
        return nodeA
    
    for exponent in range(key-1, -1, -1):
        if parent[nodeA][exponent] != parent[nodeB][exponent]:
            nodeA = parent[nodeA][exponent]
            nodeB = parent[nodeB][exponent]
        
    return parent[nodeA][0]
    
def total_cost(nodeA, nodeB):
    
    ans = 0
    
    for exponent in range(key-1, -1, -1):
        if depth[nodeA] - depth[LCA] >= (1 << exponent):
            ans += cost[nodeA][exponent]
            nodeA = parent[nodeA][exponent]
        if depth[nodeB] - depth[LCA] >= (1 << exponent):
            ans += cost[nodeB][exponent]
            nodeB = parent[nodeB][exponent]
    
    return ans

def kth_vertex(nodeA, nodeB, k):
    
    if 1 <= k <= depth[nodeA] - depth[LCA] + 1:
        k -= 1
        for exponent in range(key-1, -1, -1):
            if k >= (1 << exponent):
                k -= (1 << exponent)
                nodeA = parent[nodeA][exponent]
        return nodeA
    else:
        k = depth[nodeA] + depth[nodeB] - 2 * depth[LCA] - k + 1 
        for exponent in range(key-1, -1, -1):
            if k >= (1 << exponent):
                k -= (1 << exponent)
                nodeB = parent[nodeB][exponent]
        return nodeB
        

# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []

for edge in range(node_count - 1):
    nodeA, nodeB, weight = map(int, sys.stdin.readline().split())
    graph[nodeA].append((nodeB, weight))
    graph[nodeB].append((nodeA, weight))


# 2. TO CONSTRUCT TABLES

key = 17

parent = [[-1 for exponent in range(key)] for node in range(node_count + 1)]
cost = [[-1 for exponent in range(key)] for node in range(node_count + 1)]

depth = [-1 for node in range(node_count + 1)]
visited = [-1 for node in range(node_count + 1)]


# 6. TO SOLVE THE PROBLEM

set_depth(1, 0)
set_tables()

query_count = int(sys.stdin.readline())
for query in range(query_count):
    query_input = list(map(int, sys.stdin.readline().split()))
    query_type, nodeA, nodeB = query_input[0], query_input[1], query_input[2]
    LCA = lca(nodeA, nodeB)
    if query_type == 1:
        print(total_cost(nodeA, nodeB))
    else:
        k = query_input[3]
        print(kth_vertex(nodeA, nodeB, k))