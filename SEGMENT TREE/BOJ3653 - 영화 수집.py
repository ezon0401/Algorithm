'''
BOJ 3653 - Movie Collection (https://www.acmicpc.net/problem/3653)

DVDs from 1 to N are stacked.
After watching a DVD, customers put the DVD on top.
Whenever a customer watches a DVD, print the number of DVDs above it among the stack.
'''

import sys


# 3. FUNCTIONS TO PROCESS QUERIES

def movie_above(movie):
    
    start = movie_loc[movie] + align
    end = (1 << 19) - 1
    
    count = 0
    
    while start <= end:
        if start % 2 == 1:
            count += seg_tree[start]
            start += 1
        if end % 2 == 0:
            count += seg_tree[start]
            end -= 1
        start >>= 1
        end >>= 1
    
    return count

def watch_movie(movie):
    
    global highest
    
    delete_loc = movie_loc[movie] + align
    
    while delete_loc != 0:
        seg_tree[delete_loc] -= 1
        delete_loc >>= 1
    
    add_loc = highest + align
    movie_loc[movie] = highest
    highest += 1
    
    while add_loc != 0:
        seg_tree[add_loc] += 1
        add_loc >>= 1


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    movie_count, query_count = map(int, sys.stdin.readline().split())
    queries = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO CONSTRUCT A SEGMENT TREE
    
    align = 1 << 18
    seg_tree = [0 for index in range(1 << 19)]
    
    movie_loc = {}
    for movie in range(1, movie_count+1):
        movie_loc[movie] = 100000 - movie
        seg_tree[align + movie_loc[movie]] += 1
    for index in range(align-1, 0, -1):
        seg_tree[index] = seg_tree[index << 1] + seg_tree[(index << 1) | 1]
    
    
    # 4. TO SOLVE THE PROBLEM
    
    highest = 100000
    for query in queries:
        print(movie_above(query) - 1, end = ' ')
        watch_movie(query)
    print()