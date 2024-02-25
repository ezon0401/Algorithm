'''
BOJ 11266 - Articulation Point (https://www.acmicpc.net/problem/11266)

Given a graph, print articulation points.
'''


import sys
sys.setrecursionlimit(10 ** 5)


# 2. ARTICULATION POINT FUNCTION

def articulation_point(now, root):
    
    global dfs_count
    visited[now] = dfs_count
    dfs_count += 1
    
    result = visited[now]
    child_count = 0
    
    for after in graph[now]:
        
        if visited[after] == 0:
            
            # If a child of node X in the DFS tree cannot access a higher node without passing X, then X is an articulation point.
            child_count += 1
            child_best = articulation_point(after, False)
            if not root and child_best == visited[now]:
                ans[now] = 1
            result = min(result, child_best)

        else:
            
            result = min(result, visited[after])
    
    # A root node of the DFS tree is an articulation point if it has children in the DFS tree. 
    if root and child_count > 1:
        ans[now] = 1

    return result


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(1, node_count+1):
    graph[node] = []

for edge in range(edge_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 3. TO SOLVE THE PROBLEM

dfs_count = 1
visited = [0 for index in range(node_count+1)]
ans = [0 for index in range(node_count+1)]

for node in range(1, node_count+1):
    if visited[node] == 0:
        articulation_point(node, True)

print(sum(ans))
for node in range(1, node_count+1):
    if ans[node] == 1:
        print(node, end = ' ')