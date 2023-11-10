'''
BOJ 28330 - Wooksin-ness of a Graph (https://www.acmicpc.net/problem/28330)

Given a graph, what is the minimum number of additional edges needed to make a cycle?
'''

import sys
from collections import deque


# 2. A FUNCTION TO CHECK IF A GRAPH HAS A CYCLE (BFS)
# A graph has a cycle if a vertex to search is already visited, except for the one you searched right before.

def cycle(graph):
    
    visited = [0 for vertex in range(vertex_count)]
    cycle = False
    
    for vertex in range(vertex_count):
        if visited[vertex] == 0:
            
            bfs = deque([(vertex, -1)])
            visited[vertex] = 1
            while bfs:
                now, before = bfs.popleft()
                for next in graph[now]:
                    if visited[next] == 0:
                        bfs.append((next, now))
                        visited[next] = 1
                    else:
                        if next != before:
                            cycle = True
    
    return cycle
            
            
# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    vertex_count, edge_count = map(int, sys.stdin.readline().split())
    
    graph = {}
    for vertex in range(vertex_count):
        graph[vertex] = []
    for edge in range(edge_count):
        vertex1, vertex2 = map(int, sys.stdin.readline().split())
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    
    
    # 3. TO SOLVE THE PROBLEM
    
    if vertex_count < 3:
        print(-1)
    else:
        if cycle(graph):
            print(0)
        else:
            best = 0
            for vertex in range(vertex_count):
                if len(graph[vertex]) > best:
                    best = min(2, len(graph[vertex]))
            print(3 - best)