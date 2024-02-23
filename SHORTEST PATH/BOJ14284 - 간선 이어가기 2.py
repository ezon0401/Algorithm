'''
BOJ 14284 - Edge Connection 2 (https://www.acmicpc.net/problem/14284)

There are N nodes, and M possible edges.
A person will add an edge among M possible edges until vertex S and T is connected.
Determine the minimum sum of all edges used.
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

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = {}
for node in range(1, node_count + 1):
    graph[node] = []

for edge in range(edge_count):
    start, end, dist = map(int, sys.stdin.readline().split())
    graph[start].append((dist, end))
    graph[end].append((dist, start))

start_node, end_node = map(int, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM

print(dijkstra(start_node)[end_node])