'''
BOJ 11400 - Bridge (https://www.acmicpc.net/problem/11400)

Given a graph, print bridges.
'''

import sys
sys.setrecursionlimit(10 ** 5)


# 2. A DFS-BASED FUNCTION TO SOLVE THE PROBLEM

def solve(now, before):
    
    global dfs_count
    visited[now] = dfs_count
    dfs_count += 1
    
    result = visited[now]
    
    for after in graph[now]:
        
        if before != after:
            
            # If a child Y of node X in the DFS tree cannot access a higher node without passing X, then X-Y is a bridge.
            if visited[after] == 0:
                child_best = solve(after, now)
                result = min(result, child_best)
                if child_best > visited[now]:
                    if now < after:
                        ans.append((now, after))
                    else:
                        ans.append((after, now))
            else:
                result = min(result, visited[after])

    return result


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []

for edge in range(edge_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 3. TO SOLVE THE PROBLEM

dfs_count = 1
visited = [0 for index in range(node_count + 1)]

res = [0 for index in range(node_count + 1)]

ans = []
solve(1, -1)

ans.sort()
print(len(ans))
for nodeA, nodeB in ans:
    print(nodeA, nodeB)