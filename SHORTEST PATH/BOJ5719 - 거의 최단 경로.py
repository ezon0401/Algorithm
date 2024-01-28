'''
BOJ 5719 - THE ALMOST SHORTEST PATH (https://www.acmicpc.net/problem/5719)

Given a directed graph, calculate the length of the almost shortest path. 
The almost shortest path is the shortest path only of edges that are not a part of the shortest path.
'''

import sys, heapq


# 2. A DIJKSTRA FUNCTION

def dijkstra(start_node):

    visited = [inf for node in range(node_count)]
    
    heap = [(0, start_node)]
    visited[start_node] = 0
    
    while heap:
        now_dist, now_node = heapq.heappop(heap)
        if now_dist <= visited[now_node]:
            for next_node, next_dist in graph[now_node]:
                dist = now_dist + next_dist
                if dist < visited[next_node]:
                    visited[next_node] = dist
                    heapq.heappush(heap, (dist, next_node))
    
    return visited
    

# 1. TO GET THE INPUT

inf = float('inf')

while True:
    
    node_count, edge_count = map(int, sys.stdin.readline().split())
    if node_count == 0 and edge_count == 0:
        break
    
    graph = {}
    reverse_graph = {}
    for node in range(node_count):
        graph[node] = []
    
    start_node, end_node = map(int, sys.stdin.readline().split())
    
    for edge in range(edge_count):
        start, end, dist = map(int, sys.stdin.readline().split())
        graph[start].append((end, dist))
    
    
    # 3. TO GET SHORTEST PATHS BETWEEN ARBITRARY NODE PAIR
    
    min_dist = []
    for node in range(node_count):
        min_dist.append(dijkstra(node))
    
    
    # 4. TO SOLVE THE PROBLEM (DIJKSTRA)
    # If min_dist(start, now) + edge(now, next) + min_dist(next, end) == min_dist(start, end), then edge(now, next) is on the shortest path. 
    
    ans = [inf for node in range(node_count)]
    
    heap = [(0, start_node)]
    ans[start_node] = 0
    
    while heap:
        now_dist, now_node = heapq.heappop(heap)
        if now_dist <= ans[now_node]:
            for next_node, next_dist in graph[now_node]:
                dist = now_dist + next_dist
                if dist < ans[next_node] and min_dist[start_node][now_node] + next_dist + min_dist[next_node][end_node] != min_dist[start_node][end_node]:
                    ans[next_node] = dist
                    heapq.heappush(heap, (dist, next_node))
    
    if ans[end_node] == inf:
        print(-1)
    else:
        print(ans[end_node])