'''
BOJ 7578 - Factory (https://www.acmicpc.net/problem/7578)

There are 2N machines, N machines on two rows.
Each machine on upper row is connected to a machine on lower row by a cable.
Connected pair has same serial number and every serial number is distinct.
Calculate the number of crosses. 
'''

import sys


# 3. FUNCTIONS TO PROCESS QUERIES

def local_sum(end):
    
    start = align
    end += align
    
    result = 0
    while start <= end:
        if start % 2 == 1:
            result += seg_tree[start]
            start += 1
        if end % 2 == 0:
            result += seg_tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    
    return result

def seg_add(loc):
    
    loc += align
    while loc != 0:
        seg_tree[loc] += 1
        loc >>= 1


# 1. TO GET THE INPUT

machine_count = int(sys.stdin.readline())
upper_row = list(map(int, sys.stdin.readline().split()))
lower_row = list(map(int, sys.stdin.readline().split()))

key = {}
for index in range(machine_count):
    key[upper_row[index]] = index


# 2. TO CONSTRUCT SEGMENT TREE

align = 1 << 19
seg_tree = [0 for index in range(1 << 20)]


# 4. TO SOLVE THE PROBLEM

# Let's define the relation between machine x of the lower row and the index i of corresponding machine of the upper row as f(x) = i.
# For each machine x of the lower row, the number of crosses equals the number of x' such that x' < x and f(x') > f(x).
# The segment tree will store f(x).

cross_count = 0

for machine in lower_row:
    upper_loc = key[machine]
    cross_count += seg_tree[1] - local_sum(upper_loc)
    seg_add(upper_loc)
    
print(cross_count)