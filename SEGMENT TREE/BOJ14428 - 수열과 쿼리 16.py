'''
BOJ 14428 -Sequence and Queries 16 (https://www.acmicpc.net/problem/14428)

Given sequence A of length N, answer two queries.
(1) Change A[i] to a given value. 
(2) Print the index of the local minimum value of A[a:b+1]. 
'''

import sys


# 3. FUNCTIONS TO PROCESS QUERIES

def change_index(index, val):
    
    index += align - 1
    seg_tree[index] = [val, index - align]
    index >>= 1
    while index != 0:
        if seg_tree[index << 1][0] <= seg_tree[(index << 1) | 1][0]:
            seg_tree[index] = seg_tree[index << 1]
        else:
            seg_tree[index] = seg_tree[(index << 1) | 1]
        index >>= 1
    
def local_min(start, end):
    
    start += align - 1
    end += align - 1

    ans_val = inf
    ans_index = inf
    while start <= end:
        if start % 2 == 1:
            if seg_tree[start][0] < ans_val or (seg_tree[start][0] == ans_val and seg_tree[start][1] < ans_index):
                ans_val, ans_index = seg_tree[start]
            start += 1
        if end % 2 == 0:
            if seg_tree[end][0] < ans_val or (seg_tree[end][0] == ans_val and seg_tree[end][1] < ans_index):
                ans_val, ans_index = seg_tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    
    return ans_index


# 1. TO GET THE INPUT

arr_length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO CONSTRUCT A SEGMENT TREE

inf = float('inf')
align = 1 << 17

# The segment tree stores [local minimum value, index of the local minimum value].
seg_tree = [[inf, inf] for index in range(1 << 18)]
for index in range(align, align + arr_length):
    seg_tree[index] = [arr[index - align], index - align]
for index in range(align-1, 0, -1):
    if seg_tree[index << 1][0] <= seg_tree[(index << 1) | 1][0]:
        seg_tree[index] = seg_tree[index << 1]
    else:
        seg_tree[index] = seg_tree[(index << 1) | 1]


# 4. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())
for query in range(query_count):
    type, numA, numB = map(int, sys.stdin.readline().split())
    if type == 1:
        index, val = numA, numB
        change_index(index, val)
    else:
        start_index, end_index = numA, numB
        print(local_min(start_index, end_index) + 1)