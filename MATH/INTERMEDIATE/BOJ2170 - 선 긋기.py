'''
BOJ 2170 - Draw a Line (https://www.acmicpc.net/problem/2170)

Given lines on a horizontal line, calculate the whole length of lines.
'''

import sys


# 1. TO GET THE INPUT

line_count = int(sys.stdin.readline())

lines = []
for line in range(line_count):
    start, end = map(int, sys.stdin.readline().split())
    lines.append((start, end))
lines.sort()


# 2. TO SOLVE THE PROBLEM

ans = 0

now_start = None
now_end = None

for start, end in lines:
    
    if now_start == None and now_end == None:
        now_start = start
        now_end = end
    
    else:
        if start <= now_end:
            now_end = max(now_end, end)
        else:
            ans += now_end - now_start
            now_start = start
            now_end = end

ans += now_end - now_start

print(ans)
        