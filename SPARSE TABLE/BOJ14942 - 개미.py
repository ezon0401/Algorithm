'''
BOJ 14942 - Ants (https://www.acmicpc.net/problem/14942)

There is a weighted ant tunnel with N nodes. For every node pair (u, v), the path from u to v is unique.
At each node, there is an ant with an energy of E.
For each ant, determine the farthest node the ant can climb up. 
'''

import sys


# 3. FUNCTIONS FOR SPARSE TABLE

def set_parent(now_node):
    
    for next_node, dist in graph[now_node]:
        if not visited[next_node]:
            parent[next_node][0] = now_node
            distance[next_node][0] = dist
            visited[next_node] = visited[now_node] + 1
            set_parent(next_node)

def set_table():
    
    for exponent in range(1, 17):
        for node in range(ant_count):
            if parent[node][exponent-1] != -1:
                parent[node][exponent] = parent[parent[node][exponent-1]][exponent-1]
                distance[node][exponent] = distance[node][exponent-1] + distance[parent[node][exponent-1]][exponent-1]


# 4. FUNCTIONS TO SOLVE THE PROBLEM

def solve(ant):
    
    now_loc = ant
    energy_left = energy[ant]
    
    for exponent in range(16, -1, -1):
        if energy_left >= distance[now_loc][exponent]:
            energy_left -= distance[now_loc][exponent]
            now_loc = parent[now_loc][exponent]
            
    return now_loc + 1


# 1. TO GET THE INPUT

ant_count = int(sys.stdin.readline())

energy = [0 for ant in range(ant_count)]
for ant in range(ant_count):
    energy[ant] = int(sys.stdin.readline())

graph = {}
for ant in range(ant_count):
    graph[ant] = []
for edge in range(ant_count - 1):
    start, end, dist = map(int, sys.stdin.readline().split())
    graph[start-1].append((end-1, dist))
    graph[end-1].append((start-1, dist))


# 2. SPARSE TABLE

visited = [0 for ant in range(ant_count)]
visited[0] = 1

parent = [[-1 for exponent in range(17)] for ant in range(ant_count)]
distance = [[float('inf') for exponent in range(17)] for ant in range(ant_count)]

set_parent(0)
set_table()
    

# 5. TO SOLVE THE PROBLEM

for ant in range(ant_count):
    print(solve(ant))