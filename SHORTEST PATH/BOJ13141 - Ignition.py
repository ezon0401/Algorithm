'''
BOJ 13141 - Ignition (https://www.acmicpc.net/problem/13141)

Your goal is to burn a given graph by igniting a vertex.
Fire will move a distance of 1 for each second.
Determine the fastest time to burn the whole graph.
'''

import sys


# 1. TO GET THE INPUT

inf = float('inf')

node_count, edge_count = map(int, sys.stdin.readline().split())

edges = []

graph = [[inf for nodeB in range(node_count+1)] for nodeA in range(node_count+1)]
for edge in range(edge_count):
    start, end, length = map(int, sys.stdin.readline().split())
    graph[start][end] = min(graph[start][end], length)
    graph[end][start] = min(graph[start][end], length)
    edges.append((start, end, length))


# 2. FLOYD-WARSHALL
# The time vertex X is ignited equals the minimum distance between the start node and X. 

for node in range(1, node_count+1):
    graph[node][node] = 0

for mid in range(1, node_count+1):
    for nodeA in range(1, node_count+1):
        for nodeB in range(1, node_count+1):
            if graph[nodeA][nodeB] > graph[nodeA][mid] + graph[mid][nodeB]:
                graph[nodeA][nodeB] = graph[nodeA][mid] + graph[mid][nodeB]


# 3. TO SOLVE THE PROBLEM

ans = inf

for start_node in range(1, node_count+1):
    
    case_time = 0
    
    for start, end, length in edges:
        
        time = max(graph[start_node][start], graph[start_node][end])
        length = max(0, length - abs(graph[start_node][start] - graph[start_node][end]))
        time += length / 2
        
        case_time = max(case_time, time)
    
    ans = min(ans, case_time)

print(format(ans, ".1f"))