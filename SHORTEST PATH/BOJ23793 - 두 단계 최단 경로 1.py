'''
BOJ 23793 - Two Step Shortest Path (https://www.acmicpc.net/problem/23793)

Given a directed graph, print the following:

(1) The shortest distance of the path X -> Y -> Z.
(2) The shortest distance of the path X -> Z without visiting Y. 
'''

import sys, heapq


# 2. DIJKSTRA FUNCTION

def dijkstra(graph, start):
    
    distance = [float('inf') for node in range(node_count + 1)]
    distance[start] = 0
    
    heap = [(0, start)]
    while heap:
        now_dist, now_loc = heapq.heappop(heap)
        if now_dist <= distance[now_loc]:
            for dist, next_loc in graph[now_loc]:
                next_dist = now_dist + dist
                if next_dist < distance[next_loc]:
                    distance[next_loc] = next_dist
                    heapq.heappush(heap, (next_dist, next_loc))
    
    return distance


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph_with_mid = {}
for node in range(1, node_count + 1):
    graph_with_mid[node] = []

for edge in range(edge_count):
    start, end, dist = map(int, sys.stdin.readline().split())
    graph_with_mid[start].append((dist, end))

start_node, mid_node, end_node = map(int, sys.stdin.readline().split())

graph_without_mid = {}
for node in range(1, node_count + 1):
    graph_without_mid[node] = []

for node in range(1, node_count + 1):
    for dist, next_node in graph_with_mid[node]:
        if node != mid_node and next_node != mid_node:
            graph_without_mid[node].append((dist, next_node))


# 3. TO SOLVE THE PROBLEM

from_start = dijkstra(graph_with_mid, start_node)
from_mid = dijkstra(graph_with_mid, mid_node)

with_mid = from_start[mid_node] + from_mid[end_node]
if from_start[mid_node] == float('inf') or from_mid[end_node] == float('inf'):
    with_mid = -1

without_mid = dijkstra(graph_without_mid, start_node)[end_node]
if without_mid == float('inf'):
    without_mid = -1

print(with_mid, without_mid)