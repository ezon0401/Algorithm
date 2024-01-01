'''
BOJ 2402 - Lie (https://www.acmicpc.net/problem/2402)

There is a binary sequence of length N.
A person answers M queries: How many times does 1 appear from the i-th index to the j-th index? 
If the answer is 0, it appears even times. Otherwise, it appears odd times.
When did the person answer the query in the wrong way? 
'''

import sys


# 1. UNION FIND

def find(element):
    
    if element != parent[element]:
        parent[element] = find(parent[element])
    return parent[element]

def union(elementA, elementB):
    
    parentA = find(elementA)
    parentB = find(elementB)
    
    if parentA < parentB:
        parent[parentA] = parentB
    else:
        parent[parentB] = parentA
        
        
# 2. TO SOLVE THE PROBLEM
# If i and j are in the same group, the parity of appearance of 1 until the i-th index and the j-th index are the same. 
# If the answer is 0, i-1 and j are in the same group. Otherwise, i-1 and ~j are in the same group.

arr_length, query_count = map(int, sys.stdin.readline().split())

parent = {}

ans = query_count + 1
for query_num in range(1, query_count + 1):
    
    indexA, indexB, query_answer = map(int, sys.stdin.readline().split())
    indexB += 1
    
    if indexA not in parent:
        parent[indexA] = indexA
        parent[-indexA] = -indexA
    if indexB not in parent:    
        parent[indexB] = indexB
        parent[-indexB] = -indexB
    
    if query_answer == 1:
        union(indexA, -indexB)
        union(-indexA, indexB)
    else:
        union(indexA, indexB)
        union(-indexA, -indexB)
    
    if find(indexA) == find(-indexA) or find(indexB) == find(-indexB):
        ans = query_count
        break

print(ans)