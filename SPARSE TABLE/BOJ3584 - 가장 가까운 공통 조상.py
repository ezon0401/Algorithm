'''
BOJ 3584 - Lowest Common Ancestor (https://www.acmicpc.net/problem/3584)

Given a tree and two nodes, X and Y, print the lowest common ancestor of X and Y.
'''


import sys
sys.setrecursionlimit(10 ** 6)


# 3. DFS TO CALCULATE NODE DEPTH

def set_depth(node, node_depth):
    
    depth[node] = node_depth
    
    for child_node in graph[node]:
        parent[child_node][0] = node
        set_depth(child_node, node_depth + 1)


# 4. DP TO FILL PARENT TABLE

def set_parent():
    
    set_depth(root, 0)
    for exponent in range(1, key):
        for node_num in range(node_count):
            parent[node_num][exponent] = parent[parent[node_num][exponent-1]][exponent-1]
        
        
# 5. LCA

def lca(nodeA, nodeB):
    
    if depth[nodeA] > depth[nodeB]:
        nodeA, nodeB = nodeB, nodeA
    
    for exponent in range(key - 1, -1, -1):
        if depth[nodeB] - depth[nodeA] >= 2 ** exponent:
            nodeB = parent[nodeB][exponent]
    
    if nodeA == nodeB:
        return nodeA
    else:
        for exponent in range(key - 1, -1, -1):
            if parent[nodeA][exponent] != parent[nodeB][exponent]:
                nodeA = parent[nodeA][exponent]
                nodeB = parent[nodeB][exponent]
    
    return parent[nodeA][0]


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    node_count = int(sys.stdin.readline())
    key = 14
    
    
    # 2. TO CREATE A TABLE
    
    parent = [[-1 for exponent in range(key)] for node_num in range(node_count)]
    depth = [-1 for node_num in range(node_count)]
    
    graph = {}
    for node_num in range(node_count):
        graph[node_num] = []
    
    for edge in range(node_count - 1):
        parent_node, child_node = map(int, sys.stdin.readline().split())
        graph[parent_node-1].append(child_node-1)
        parent[child_node-1][0] = parent_node - 1
    
    root = -1
    for node_num in range(node_count):
        if parent[node_num][0] == -1:
            root = node_num
            break
    
    
    # 6. TO SOLVE THE PROBLEM
    
    set_parent()
    
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    print(lca(nodeA-1, nodeB-1) + 1)