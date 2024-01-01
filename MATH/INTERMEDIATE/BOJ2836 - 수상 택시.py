'''
BOJ 2836 - Water Taxi (https://www.acmicpc.net/problem/2836)

A water taxi has to give a ride to N guests. Each guest has a destination.
After giving a ride to all guests, the taxi has to go to location X. 
The taxi is big enough to take N guests at the same time.
Determine the minimum length of the taxi route. 
'''

import sys


# 1. TO GET THE INPUT

guest_count, goal = map(int, sys.stdin.readline().split())

forward_path = []
reverse_path = []
for guest_path in range(guest_count):
    start, end = map(int, sys.stdin.readline().split())
    if start <= end:
        forward_path.append((start, end))
    else:
        reverse_path.append((start, end))
    
forward_path.sort()
reverse_path.sort(reverse=True)


# 2. SWEEPING

combined_reverse_path = []

for start, end in reverse_path:
    if len(combined_reverse_path) == 0:
        combined_reverse_path.append((start, end))
    else:
        now_start, now_end = start, end
        while len(combined_reverse_path) != 0 and now_start >= combined_reverse_path[-1][1]:
            last_start, last_end = combined_reverse_path.pop()
            now_start, now_end = max(last_start, now_start), min(last_end, now_end)
        combined_reverse_path.append((now_start, now_end))


# 3. TO SOLVE THE PROBLEM

ans = 0

# Every forward-direction route can be considered by just moving forward. 
forward_max = 0
for start, end in forward_path:
    forward_max = max(end, forward_max)
for start, end in combined_reverse_path:
    forward_max = max(start, forward_max)
ans += forward_max

# How to process reverse-direction routes depends on the location of the destination and goal.
ans += abs(forward_max - goal)
for start, end in combined_reverse_path:
    if goal <= end:
        continue
    elif end < goal < start:
        ans += (goal - end) * 2
    else:
        ans += (start - end) * 2

print(ans)