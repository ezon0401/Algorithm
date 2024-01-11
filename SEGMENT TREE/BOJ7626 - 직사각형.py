'''
BOJ 7626 - Rectangles (https://www.acmicpc.net/problem/7626)

There are N rectangles on a plane.
Calculate the area covered by the rectangles. 
'''

import sys


# 4. FUNCTIONS TO PROCESS QUERIES

def parent_add(now, val):
    
    while now != 0 and count[now >> 1] == 0:
        seg_tree[now >> 1] += val
        now >>= 1
        
def parent_delete(now, val):
    
    while now != 0 and count[now >> 1] == 0:
        seg_tree[now >> 1] -= val
        now >>= 1
    
def add_line(y1, y2):
    
    start = align + compress_y[y1]
    end = align + compress_y[y2] - 1
    
    while start <= end:
        if start % 2 == 1:
            to_add = max_val[start] - seg_tree[start]
            seg_tree[start] = max_val[start]
            parent_add(start, to_add)
            count[start] += 1
            start += 1
        if end % 2 == 0:
            to_add = max_val[end] - seg_tree[end]
            seg_tree[end] = max_val[end]
            parent_add(end, to_add)
            count[end] += 1
            end -= 1
        start >>= 1
        end >>= 1

def delete_line(y1, y2):

    start = align + compress_y[y1]
    end = align + compress_y[y2] - 1
    
    while start <= end:
        if start % 2 == 1:
            count[start] -= 1
            if count[start] == 0:
                if start >= align:
                    to_delete = seg_tree[start]
                    seg_tree[start] = 0
                else:
                    child_sum = seg_tree[start << 1] + seg_tree[(start << 1) | 1]
                    to_delete = seg_tree[start] - child_sum
                    seg_tree[start] = child_sum
                parent_delete(start, to_delete)
            start += 1
        if end % 2 == 0:
            count[end] -= 1
            if count[end] == 0:
                if end >= align:
                    to_delete = seg_tree[end]
                    seg_tree[end] = 0
                else:
                    child_sum = seg_tree[end << 1] + seg_tree[(end << 1) | 1]
                    to_delete = seg_tree[end] - child_sum
                    seg_tree[end] = child_sum
                parent_delete(end, to_delete)
            end -= 1
        start >>= 1
        end >>= 1
    
    
# 1. TO GET THE INPUT
# 0 denotes start lines and 1 denotes end lines. 

rectangle_count = int(sys.stdin.readline())

lines = []
y_coordinate = set()

for rectangle in range(rectangle_count):
    x1, x2, y1, y2 = map(int, sys.stdin.readline().split())
    lines.append((x1, y1, y2, 0))
    lines.append((x2, y1, y2, 1))
    y_coordinate.add(y1)
    y_coordinate.add(y2)

lines.sort()


# 2. COORDINATE COMPRESSION

compress_y = {}
length = [0 for index in range((1 << 19) | 1)]

y_coordinate = sorted(list(y_coordinate))
for index in range(len(y_coordinate)):
    compress_y[y_coordinate[index]] = index

for index in range(len(y_coordinate) - 1):
    length[index] = y_coordinate[index+1] - y_coordinate[index]


# 3. TO CONSTRUCT A SEGMENT TREE

align = 1 << 19
seg_tree = [0 for index in range(1 << 20)]
count = [0 for index in range(1 << 20)]

max_val = [0 for index in range(1 << 20)]
for index in range(align, (1 << 20)):
    max_val[index] = length[index - align]
for index in range(align-1, 0, -1):
    max_val[index] = max_val[index << 1] + max_val[(index << 1) | 1]


# 5. TO SOLVE THE PROBLEM
# For each x, add the length of valid lines. 

ans = 0
before_x = 0
for line in lines:
    x, y1, y2, type = line
    ans += (x - before_x) * seg_tree[1]
    before_x = x
    if type == 0:
        add_line(y1, y2)
    else:
        delete_line(y1, y2)
print(ans)