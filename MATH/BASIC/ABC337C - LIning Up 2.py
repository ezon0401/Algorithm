'''
ABC337C - Lining Up 2 (https://atcoder.jp/contests/abc337/tasks/abc337_c)

N people are standing in a line.
For each person, a person right in front of him is given.
Print the line from front to back.
'''

import sys


# 1. TO GET THE INPUT

people_count = int(sys.stdin.readline())
front = list(map(int, sys.stdin.readline().split()))


# 2. TO CONSTRUCT A LINKED LIST AND SOLVE THE PROBLEM

graph = [-1 for person in range(people_count + 1)]

start = None
for person in range(people_count):
    if front[person] != -1:
        graph[front[person]] = person + 1
    else:
        start = person + 1

while start != -1:
    print(start, end = ' ')
    start = graph[start]