'''
BOJ 17396 - Backdoor (https://www.acmicpc.net/problem/17396)

Given a graph and passable nodes, print the shortest distance from node 0 to N-1.
'''

import sys, heapq


# 2. DIJKSTRA FUNCTION

def dijkstra(start):
    
    distance = [float('inf') for node in range(node_count)]
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
impossible = list(map(int, sys.stdin.readline().split()))
impossible[-1] = 0
    
graph = {}
for node in range(node_count):
    graph[node] = []
    
for edge in range(edge_count):
    nodeA, nodeB, dist = map(int, sys.stdin.readline().split())
    if not impossible[nodeA] and not impossible[nodeB]:
        graph[nodeA].append((dist, nodeB))
        graph[nodeB].append((dist, nodeA))


# 3. TO SOLVE THE PROBLEM

ans = dijkstra(0)[-1]
if ans == float('inf'):
    ans = -1
print(ans)