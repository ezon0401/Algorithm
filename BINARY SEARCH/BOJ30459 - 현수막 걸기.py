'''
BOJ 30459 - Banner Hanging (https://www.acmicpc.net/problem/30459)

There are N posts and M flag poles.
The distance between two posts is the baseline of a triangle, and the length of a flag pole is the height.
If the area of a banner cannot exceed R, what is the maximum area of a banner?
'''

import sys


# 1. TO GET THE INPUT

post_count, pole_count, max_area = map(int, sys.stdin.readline().split())
post = list(map(int, sys.stdin.readline().split()))
pole = list(map(int, sys.stdin.readline().split()))

pole.sort()


# 2. TO SOLVE THE PROBLEM
# The question for parametric search would be "Does the area of a banner exceed R"?

ans = -1

for index1 in range(post_count):
    for index2 in range(index1+1, post_count):
        
        base = abs(post[index1] - post[index2])
        
        # If the answer is "Yes" for the shortest pole.
        if base * pole[0] > max_area * 2:
            continue
        
        # If the answer is "No" for the longest pole.
        elif base * pole[-1] <= max_area * 2:
            if ans * 2 < base * pole[-1]:
                ans = base * pole[-1] / 2
        
        # Parametric Search
        else:
            left = 0
            right = pole_count - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if base * pole[mid] <= max_area * 2:
                    left = mid
                else:
                    right = mid
            ans = max(ans, base * pole[left] / 2)

if ans == -1:
    print(ans)
else:
    print(format(ans, ".1f"))