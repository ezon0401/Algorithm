'''
BOJ 2243 - Candy Box (https://www.acmicpc.net/problem/2243)

Given a box with N candies, process the following queries:
(1) Take out the K-th most delicious candy.
(2) Add X candies with taste Y. 
'''

import sys


# 2. FUNCTIONS FOR QUERIES

def pick_Nth(N):
    
    now = 1
    while now < align:
        if seg_tree[now << 1] >= N:
            now = (now << 1)
        else:
            N -= seg_tree[now << 1]
            now = (now << 1) | 1
    
    taste = now - align
    add_candy(taste, -1)
    
    return taste
    
def add_candy(taste, count):
    
    now = taste + align
    
    while now != 0:
        seg_tree[now] += count
        now >>= 1


# 1. TO GET THE INPUT AND CONSTRUCT A SEGMENT TREE

query_count = int(sys.stdin.readline())

align = 1 << 20
seg_tree = [0 for index in range(1 << 21)]


# 3. TO SOLVE THE PROBLEM

for query_input in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    if query[0] == 1:
        print(pick_Nth(query[1]))
    else:
        add_candy(query[1], query[2])