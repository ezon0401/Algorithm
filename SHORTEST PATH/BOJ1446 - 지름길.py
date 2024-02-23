'''
BOJ 1446 - Shortcut (https://www.acmicpc.net/problem/1446)

There is a highway of length D. 
Given N shortcuts, print the shortest distance from point 0 to point D.
'''

import sys, heapq


# 2. DIJKSTRA FUNCTION

def dijkstra(start):
    
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

edge_count, node_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(node_count + 1):
    graph[node] = []
    if node != node_count:
        graph[node].append((1, node+1))

for edge in range(edge_count):
    start, end, dist = map(int, sys.stdin.readline().split())
    if end <= node_count:
        graph[start].append((dist, end))


# 3. TO SOLVE THE PROBLEM

print(dijkstra(0)[node_count])