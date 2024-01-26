'''
BOJ 1948 - Critical Path (https://www.acmicpc.net/problem/1948)

Given a directed acyclic graph, print the length of a critical path and the number of edges included in critical paths.
'''

import sys
from collections import deque


# 1. TO GET THE INPUT

city_count = int(sys.stdin.readline())
road_count = int(sys.stdin.readline())

in_degree = [0 for city in range(city_count+1)]
graph = {}
for city in range(1, city_count+1):
    graph[city] = []

reverse_graph = {}
for city in range(1, city_count+1):
    reverse_graph[city] = []

for road in range(road_count):
    start, end, dist = map(int, sys.stdin.readline().split())
    graph[start].append((end, dist))
    in_degree[end] += 1
    reverse_graph[end].append((start, dist))


# 2. TO CALCULATE THE LENGTH OF A CRITICAL PATH (TOPOLOGICAL SORT)

start_city, end_city = map(int, sys.stdin.readline().split())

distance = [0 for city in range(city_count+1)]

t_sort = deque([(start_city, 0)])

while t_sort:
    
    now_loc, now_dist = t_sort.popleft()
    for next_loc, dist in graph[now_loc]:
    
        next_dist = now_dist + dist
        if next_dist > distance[next_loc]:
            distance[next_loc] = next_dist
        
        in_degree[next_loc] -= 1
        if in_degree[next_loc] == 0:
            t_sort.append((next_loc, distance[next_loc]))

print(distance[end_city])


# 3. TO CALCULATE THE NUMBER OF EDGES INCLUDED IN CRITICAL PATHS (BFS)

ans = 0

visited = [0 for city in range(city_count+1)]
visited[end_city] = 1

bfs = deque([(end_city, distance[end_city])])

while bfs:
    
    now_loc, now_left = bfs.popleft()
    for next_loc, dist in reverse_graph[now_loc]:
        
        next_left = now_left - dist
        if next_left == distance[next_loc]:
            ans += 1
            if visited[next_loc] == 0:
                visited[next_loc] = 1
                bfs.append((next_loc, distance[next_loc]))

print(ans)