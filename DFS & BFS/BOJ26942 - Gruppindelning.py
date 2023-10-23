'''
BOJ 26942 - Grouping (https://www.acmicpc.net/problem/26942)

Student names and friend relationships are given.
Calculate the maximum number of groups when friends are in the same group.
'''

import sys
from collections import deque


# 2. BFS

def bfs(start):
    
    queue = deque([start])
    while queue:
        now_student = queue.popleft()
        for next_student in graph[now_student]:
            if visited[next_student] == 0:
                visited[next_student] = 1
                queue.append(next_student)


# 1. TO GET THE INPUT

student_count = int(sys.stdin.readline())

student_to_num = {}
for student_num in range(student_count):
    name = sys.stdin.readline().strip()
    student_to_num[name] = student_num

# To construct a graph

graph = {}
for student_num in range(student_count):
    graph[student_num] = []

relation_count = int(sys.stdin.readline())
for relation_input in range(relation_count):
    studentA, studentB = sys.stdin.readline().strip().split()
    studentA_num = student_to_num[studentA]
    studentB_num = student_to_num[studentB]
    graph[studentA_num].append(studentB_num)
    graph[studentB_num].append(studentA_num)


# 3. TO SOLVE THE PROBLEM
# The problem is equivalent to calculating the number of connected components.

ans = 0

visited = [0 for student_num in range(student_count)]
for student_num in range(student_count):
    if visited[student_num] == 0:
        visited[student_num] = 1
        ans += 1
        bfs(student_num)

print(ans)

