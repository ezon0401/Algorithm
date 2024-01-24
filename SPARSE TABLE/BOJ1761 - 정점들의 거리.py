'''
BOJ 1761 - Distance between Vertices (https://www.acmicpc.net/problem/1761)

Given a tree with N vertices, answer M queries: Calculate the distance between two nodes A and B.
'''

import sys
sys.setrecursionlimit(10 ** 5)


# 3. FUNCTIONS TO SET SPARSE TREES

def set_depth(node, node_depth):
    
    depth[node] = node_depth
    visited[node] = 1
    
    for next_node, dist in graph[node]:
        if visited[next_node] == -1:
            parent[next_node][0] = node
            distance[next_node][0] = dist
            set_depth(next_node, node_depth + 1)

def set_parent():
    
    for exponent in range(1, key):
        for node in range(1, node_count + 1):
            if parent[node][exponent-1] != -1:
                parent[node][exponent] = parent[parent[node][exponent-1]][exponent-1]
                if distance[parent[node][exponent-1]][exponent-1] != -1:
                    distance[node][exponent] = distance[node][exponent-1] + distance[parent[node][exponent-1]][exponent-1]


# 4. LCA-RELATED FUNCTIONS TO SOLVE THE PROBLEM

def lca(nodeA, nodeB):
    
    if depth[nodeA] > depth[nodeB]:
        nodeA, nodeB = nodeB, nodeA
    
    for exponent in range(key-1, -1, -1):
        if depth[nodeB] - depth[nodeA] >= pow(2, exponent):
            nodeB = parent[nodeB][exponent]
    
    if nodeA == nodeB:
        return nodeA
    else:
        for exponent in range(key-1, -1, -1):
            if parent[nodeA][exponent] != parent[nodeB][exponent]:
                nodeA = parent[nodeA][exponent]
                nodeB = parent[nodeB][exponent]
    
    return parent[nodeA][0]

def dist_between_nodes(nodeA, nodeB):
    
    target = lca(nodeA, nodeB)
    result = 0
    
    for exponent in range(key-1, -1, -1):
        if depth[nodeA] - depth[target] >= pow(2, exponent):
            result += distance[nodeA][exponent]
            nodeA = parent[nodeA][exponent]
    
    for exponent in range(key-1, -1, -1):
        if depth[nodeB] - depth[target] >= pow(2, exponent):
            result += distance[nodeB][exponent]
            nodeB = parent[nodeB][exponent]
    
    return result
    

# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []

for edge in range(node_count-1):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    graph[nodeA].append((nodeB, dist))
    graph[nodeB].append((nodeA, dist))


# 2. TO CONSTRUCT SPARSE TREES

key = 16

depth = [-1 for node in range(node_count+1)]
visited = [-1 for node in range(node_count+1)]

parent = [[-1 for exponent in range(key)] for node in range(node_count+1)]
distance = [[-1 for exponent in range(key)] for node in range(node_count+1)]

set_depth(1, 1)
set_parent()


# 5. TO SOLVE THE PROBELM

query_count = int(sys.stdin.readline())
for query in range(query_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    print(dist_between_nodes(nodeA, nodeB))