'''
BOJ 11438 - LCA 2 (https://www.acmicpc.net/problem/11438)

Given a tree, answer queries: What is the lowest common ancestor of nodes X and Y?
'''

import sys
sys.setrecursionlimit(10 ** 6)


# 2. A FUNCTION TO SET NODE DEPTH

def set_depth(node, node_depth):

    depth[node] = node_depth
    visited[node] = 1
    
    for next_node in graph[node]:
        if visited[next_node] == -1:
            set_depth(next_node, node_depth + 1)
            parent[next_node][0] = node


# 3. A FUNCTION TO FILL PARENT TABLE

def set_parent():
    
    for exponent in range(1, key):
        for node in range(node_count):
            parent[node][exponent] = parent[parent[node][exponent-1]][exponent-1]
            

# 4. LCA

def lca(nodeA, nodeB):
    
    if depth[nodeA] > depth[nodeB]:
        nodeA, nodeB = nodeB, nodeA
        
    # To level the depth of nodeA and nodeB
    for exponent in range(key-1, -1, -1):
        if depth[nodeB] - depth[nodeA] >= 2 ** exponent:
            nodeB = parent[nodeB][exponent]
    
    # To find LCA
    if nodeA == nodeB:
        return nodeA + 1
    else:
        for exponent in range(key-1, -1, -1):
            if parent[nodeA][exponent] != parent[nodeB][exponent]:
                nodeA = parent[nodeA][exponent]
                nodeB = parent[nodeB][exponent]
    
    return parent[nodeA][0] + 1


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

graph = {}
for node in range(node_count):
    graph[node] = []
    
for edge in range(node_count - 1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    graph[nodeA-1].append(nodeB-1)
    graph[nodeB-1].append(nodeA-1)


# 5. TO SOLVE THE PROBLEM

key = 17

depth = [-1 for node in range(node_count)]
visited = [-1 for node in range(node_count)]
parent = [[-1 for exponent in range(key)] for node in range(node_count)]

set_depth(0, 0)
set_parent()

query_count = int(sys.stdin.readline())
for query in range(query_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    print(lca(nodeA-1, nodeB-1))