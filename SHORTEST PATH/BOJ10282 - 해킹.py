'''
BOJ 10282 - Hacking (https://www.acmicpc.net/problem/10282)

Given a node in a directed graph, print the number of reachable vertices and the shortest distance to the farthest node.
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

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    node_count, edge_count, start_node = map(int, sys.stdin.readline().split())
    
    graph = {}
    for node in range(1, node_count + 1):
        graph[node] = []
    
    for edge in range(edge_count):
        end, start, dist = map(int, sys.stdin.readline().split())
        graph[start].append((dist, end))


    # 3. TO SOLVE THE PROBLEM

    distance = dijkstra(start_node)
    
    count = 0
    time = 0
    for index in range(1, node_count+1):
        if distance[index] != float('inf'):
            count += 1
            if time < distance[index]:
                time = distance[index]
    
    print(count, time)

