'''
BOJ 30622 - Rush & Slash (https://www.acmicpc.net/problem/30622)

A gardener repeats the following steps to remove all the grasses.

1. Move to the location of a grass.
2. Slash it. Any connected grasses will also be slashed. 
3. Move to (0, 0). However, if there is no more grass to slash, the gardener does not move to (0, 0).

Grass A and grass B are connected if they are horizontally, vertically, or diagonally adjacent.
If grass A and grass B are connected, and grass B and grass C are connected, then grass A and grass C are also connected.

Determine the minimum distance the gardener should move to slash all the grasses.
'''

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)


# 2. UNION FIND

def find(grass):
    
    if parent[grass] != grass:
        parent[grass] = find(parent[grass])
    return parent[grass]

def union(grass1, grass2):
    
    parent1 = find(grass1)
    parent2 = find(grass2)
    if parent1 <= parent2:
        parent[parent1] = parent2
    else:
        parent[parent2] = parent1


# 1. TO GET INPUT

grass_count = int(sys.stdin.readline())

parent = {}
visited = {}

garden = []
for grass_input in range(grass_count):
    x, y = map(int, sys.stdin.readline().split())
    garden.append((x, y))
    parent[(x, y)] = (x, y)
    visited[(x, y)] = 0


# 3. TO UNION CONNECTED GRASSES

# Vertically adjacent
garden.sort()
for index in range(1, grass_count):
    if garden[index-1][0] == garden[index][0] and garden[index][1] - garden[index-1][1] == 1:
        union(garden[index-1], garden[index])

# Horizontally adjacent
garden.sort(key = lambda x : (x[1], x[0]))
for index in range(1, grass_count):
    if garden[index-1][1] == garden[index][1] and garden[index][0] - garden[index-1][0] == 1:
        union(garden[index-1], garden[index])

# Vertically adjacent
garden.sort(key = lambda x : (x[0] - x[1], x[0]))
for index in range(1, grass_count):
    if (garden[index][0] - garden[index][1]) == (garden[index-1][0] - garden[index-1][1]) and garden[index][0] - garden[index-1][0] == 1:
        union(garden[index-1], garden[index])
        
garden.sort(key = lambda x : (x[0] + x[1], x[0]))
for index in range(1, grass_count):
    if (garden[index][0] + garden[index][1]) == (garden[index-1][0] + garden[index-1][1]) and garden[index][0] - garden[index-1][0] == 1:
        union(garden[index-1], garden[index])


# 4. TO SOLVE THE PROBLEM

garden.sort(key = lambda x : abs(x[0]) + abs(x[1]))

dist = 0
last = 0
for grass in garden:
    if visited[find(grass)] == 0:
        visited[find(grass)] = 1
        dist += (abs(grass[0]) + abs(grass[1])) * 2
        last = abs(grass[0]) + abs(grass[1])

print(dist - last)