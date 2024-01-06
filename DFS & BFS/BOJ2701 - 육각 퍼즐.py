'''
BOJ 2701 - Hexagon Puzzle (https://www.acmicpc.net/problem/2701)

There is a room with 2 doors: "#" is a door, "." is an empty cell, "*" is a wall, and "!" is where a two-way mirror can be positioned.
The goal is to see the other door from one door using two-way mirrors.
Determine the minimum number of mirrors required.
'''

import sys
from collections import deque
from itertools import permutations


# 2. FUNCTIONS TO MAKE THE CODE MORE CLEAN

# Change a state into a string
def to_string(arr):
    return "".join(map(str, arr))

# Connect two states
def connect_edge(state, blank, loc):
    state_key = to_string(state)
    next_state = state[:]
    next_state[blank], next_state[loc] = next_state[loc], next_state[blank]
    graph[state_key].append((to_string(next_state), next_state[blank]))


# 1. TO CONSTRUCT A GRAPH
# If it is possible to make state B by moving a cell from state A, connect them.

graph = {}
ans = {}

states = list(map(list, permutations('ABCDEFX', 7)))

for state in states:
    state_key = to_string(state)
    graph[state_key] = []
    ans[state_key] = [None, None]

for state in states:
    
    blank = state.index("X")
        
    if blank != 6:
        connect_edge(state, blank, (blank + 1) % 6)
        connect_edge(state, blank, (blank - 1) % 6)
    else:
        connect_edge(state, blank, 1)
        connect_edge(state, blank, 4)
        
    if blank == 1 or blank == 4:
        connect_edge(state, blank, 6)


# 3. BFS 

queue = deque(['ABCDEFX'])
ans['ABCDEFX'] = [0, '']

while queue:
    now = queue.popleft()
    for next_state, moved_char in graph[now]:
        if ans[next_state][0] == None:
            ans[next_state][0] = ans[now][0] + 1
            ans[next_state][1] = ans[now][1] + moved_char
            queue.append(next_state)


# 4. TO SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())
for test in range(test_count):
    start = sys.stdin.readline().strip() + "X"
    if ans[start][0] == None:
        print(-1)
    else:
        print(ans[start][0], ans[start][1][::-1])