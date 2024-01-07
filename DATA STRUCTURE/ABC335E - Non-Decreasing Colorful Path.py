'''
ABC332E - Non-Decreasing Colorful Path (https://atcoder.jp/contests/abc335/tasks/abc335_e)

There is a connected undirected graph with weighted vertices.
For a simple path from vertex 1 to vertex N, the score of a path is 0 if the sequence of weights written on the vertices is not non-decreasing.
Otherwise, the score of the path is a number of distinct weights.
Determine the highest score.
'''

import sys, heapq


# 1. TO GET THE INPUT

vertex_count, edge_count = map(int, sys.stdin.readline().split())

weight = [0] + list(map(int, sys.stdin.readline().split()))

graph = {}
for vertex in range(1, vertex_count + 1):
    graph[vertex] = []

for edge in range(edge_count):
    vertexA, vertexB = map(int, sys.stdin.readline().split())
    graph[vertexA].append(vertexB)
    graph[vertexB].append(vertexA)


# 2. TO SOLVE THE PROBLEM

score = [0 for vertex in range(vertex_count + 1)]
score[1] = 1

heap = [(weight[1], 1)]
while heap:
    now_weight, now_loc = heapq.heappop(heap)
    for next_loc in graph[now_loc]:
        if now_weight < weight[next_loc] and score[now_loc] + 1 > score[next_loc]:
            heapq.heappush(heap, (weight[next_loc], next_loc))
            score[next_loc] = score[now_loc] + 1
        if now_weight == weight[next_loc] and score[now_loc] > score[next_loc]:
            heapq.heappush(heap, (weight[next_loc], next_loc))
            score[next_loc] = score[now_loc]
    
print(score[vertex_count])