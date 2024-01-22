'''
BOJ 13334 - Railroads (https://www.acmicpc.net/problem/13334)

There are N segments.
Determine the maximum possible number of segments that can be covered by a segment of length L.
'''

import sys
from bisect import bisect_right


# 4. FUNCTIONS TO SOLVE THE PROBLEM

def seg_delete(end):
    
    end = align + compressed_end[end]
    while end != 0:
        seg_tree[end] -= 1
        end >>= 1

def local_sum(left, right):
    
    left += align
    right += align

    result = 0
    while left <= right:
        if left % 2 == 1:
            result += seg_tree[left]
            left += 1
        if right % 2 == 0:
            result += seg_tree[right]
            right -= 1
        left >>= 1
        right >>= 1
        
    return result


# 1. TO GET THE INPUT

line_count = int(sys.stdin.readline())

end_point = []

lines = []
for line in range(line_count):
    start, end = map(int, sys.stdin.readline().split())
    if start > end:
        start, end = end, start
    lines.append((start, end))
    end_point.append(end)
lines.sort()

length = int(sys.stdin.readline())


# 2. COORDINATE COMPRESSION

compressed_end = {}
end_point_set = sorted(list(set(end_point)))

for index in range(len(end_point_set)):
    compressed_end[end_point_set[index]] = index


# 3. TO CONSTRUCT SEGMENT TREE

align = 1 << 17
seg_tree = [0 for index in range(1 << 18)]

for end in end_point:
    seg_tree[align + compressed_end[end]] += 1
for index in range(align-1, 0, -1):
    seg_tree[index] = seg_tree[index << 1] + seg_tree[(index << 1) | 1]


# 5. TO SOLVE THE PROBLEM

ans = 0
for start, end in lines:
    right = bisect_right(end_point_set, start + length) - 1
    if right != -1:
        ans = max(ans, local_sum(0, right))
    seg_delete(end)
print(ans)