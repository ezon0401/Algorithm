'''
BOJ 14808 - Pony Express (Large) (https://www.acmicpc.net/problem/14808)

There are N cities and Q queries. Every city has a horse with a different speed and stamina.
Answer queries: What is the minimum time cost from city A to city B by riding horse(s)?
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test_num in range(1, test_count + 1):
    
    city_count, query_count = map(int, sys.stdin.readline().split())
    
    horse_stamina = []
    horse_speed = []
    for city_num in range(city_count):
        stamina, speed = map(int, sys.stdin.readline().split())
        horse_stamina.append(stamina)
        horse_speed.append(speed)
    
    graph = []
    for city_num in range(city_count):
        path = list(map(int, sys.stdin.readline().split()))
        for index in range(city_count):
            if path[index] == -1:
                path[index] = float('inf')
        graph.append(path)
    
    
    # 2. FLOYD-WARSHALL
    # graph[start][end] = Minimum distance from start vertex to end vertex
    
    for city in range(city_count):
        graph[city][city] = 0
    for mid in range(city_count):
        for start in range(city_count):
            for end in range(city_count):
                if graph[start][mid] + graph[mid][end] < graph[start][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]
    
    
    # 3. TO CONVERT THE GRAPH INTO TIME COST GRAPH
    # graph[start][end] = Time cost when moving from city vertex to end vertex by riding horse of city vertex
    
    for city in range(city_count):
        for end in range(city_count):
            if graph[city][end] <= horse_stamina[city]:
                graph[city][end] = graph[city][end] / horse_speed[city]
            else:
                graph[city][end] = float('inf')
    
    
    # 4. FLOYD-WARSHALL
    # graph[start][end] = Minimum time cost to reach end vertex from start vertex
    
    for mid in range(city_count):
        for start in range(city_count):
            for end in range(city_count):
                if graph[start][mid] + graph[mid][end] < graph[start][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]
    
    
    # 5. TO SOLVE THE PROBLEM
    
    ans = []
    for query_input in range(query_count):
        start, end = map(int, sys.stdin.readline().split())
        ans.append(graph[start-1][end-1])
    
    print("Case #{}: {}".format(test_num, " ".join(map(str, ans))))