'''
BOJ 13907 - Tax (https://www.acmicpc.net/problem/13907)

There is a weighted undirected graph.
Whenever a government increases tax by X, the weight of each edge increases by X.
Print a minimum cost from vertex A to B whenever a government increases tax.
'''

import sys, heapq


# 1. TO GET THE INPUT

inf = float('inf')

city_count, road_count, tax_increase_count = map(int, sys.stdin.readline().split())
start_city, end_city = map(int, sys.stdin.readline().split())

graph = {}
for city in range(1, city_count+1):
    graph[city] = []

for road in range(road_count):
    cityA, cityB, cost = map(int, sys.stdin.readline().split())
    graph[cityA].append((cost, cityB))
    graph[cityB].append((cost, cityA))


# 2. DIJKSTRA
# visited[i][j] = The minimum cost to city i with j edges

visited = [[inf for road_in_path in range(city_count)] for city in range(city_count + 1)]
visited[start_city][0] = 0

heap = [(0, 0, start_city)]
while heap:
    
    now_cost, now_road_in_path, now_city = heapq.heappop(heap)
    
    check = True
    for road_in_path in range(now_road_in_path + 1):
        if now_cost > visited[now_city][road_in_path]:
            check = False
    
    if check:
        for cost, next_city in graph[now_city]:
            next_cost = now_cost + cost
            next_road_in_path = now_road_in_path + 1
            if next_road_in_path < city_count and next_cost < visited[next_city][next_road_in_path]:
                visited[next_city][next_road_in_path] = next_cost
                heapq.heappush(heap, (next_cost, next_road_in_path, next_city))

print(min(visited[end_city]))


# 3. TO SOLVE THE PROBLEM

for tax_increase in range(tax_increase_count):
    tax = int(sys.stdin.readline())
    for road_in_path in range(city_count):
        visited[end_city][road_in_path] += tax * road_in_path
    print(min(visited[end_city]))