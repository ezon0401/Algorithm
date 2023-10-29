'''
BOJ 11336 - Matrix (https://www.acmicpc.net/problem/11336)

The initial locations of Neo, agents, and telephones are given on a graph.
Determine if there is a path Neo can arrive at a telephone without running into an agent.
If possible, print the shortest time Neo can reach the telephone. Otherwise, print "Neo may fight an Agent".
'''

import sys
import heapq


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test_input in range(test_count):
    
    vertex_count, edge_count, agent_count, phone_count = map(int, sys.stdin.readline().split())
    
    graph = {}
    for vertex_num in range(vertex_count):
        graph[vertex_num] = []
    
    for edge_input in range(edge_count):
        start, end, dist = map(int, sys.stdin.readline().split())
        graph[start].append((end, dist))
        graph[end].append((start, dist))
    
    agent_loc = []
    for agent_input in range(agent_count):
        agent = int(sys.stdin.readline())
        agent_loc.append(agent)
    phone_loc = []
    for phone_input in range(phone_count):
        phone = int(sys.stdin.readline())
        phone_loc.append(phone)
    
    
    # 2. TO MOVE AGENTS AND NEO
    # The algorithm is similar to Dijkstra.
    
    # The array stores an array [time, person_type]. It indicates who visited the location first and when. Number 1 represents Neo, and number 2 represents agents for person_type.
    
    visited = [[float('inf'), 0] for vertex in range(vertex_count)]
    
    # The heap stores a tuple (time, person_type, location). It indicates what location Neo or an agent is after the time passes. Number 1 represents Neo, and number 2 represents agents for person_type.
    
    heap = [(0, 1, 0)]
    visited[0] = [0, 1]
    for loc in agent_loc:
        heap.append((0, 2, loc))
        visited[loc] = [0, 2]
    heapq.heapify(heap)
    
    while heap:
        now_time, now_type, now_loc = heapq.heappop(heap)
        if now_time <= visited[now_loc][0]:
            for next_loc, dist in graph[now_loc]:
                next_time = now_time + dist
                if (next_time < visited[next_loc][0]) or (next_time == visited[next_loc][0] and now_type > visited[next_loc][1]):
                    visited[next_loc] = [next_time, now_type]
                    heapq.heappush(heap, (next_time, now_type, next_loc))
        
        
    # 3. TO SOLVE A PROBLEM
    
    fight = True
    escape_time = float('inf')

    for phone in phone_loc:
        time, person_type = visited[phone]
        if person_type == 1 and time < escape_time:
            fight = False
            escape_time = time
    
    if fight:
        print("Neo may fight an Agent")
    else:
        print(escape_time)