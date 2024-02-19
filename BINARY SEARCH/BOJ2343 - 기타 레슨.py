'''
BOJ 2343 - Guitar Lesson (https://www.acmicpc.net/problem/2343)

There are N lecture videos and M blu-ray discs of the same size.
Determine the minimum size of each blu-ray disc to store all videos.
The order of the video should not change.
'''

import sys


# 2. A FUNCTION TO CHECK WHETHER A GIVEN SIZE IS POSSIBLE

def check(bluray_size):
    
    bluray_used = 1
    size_used = 0
    
    for lecture in lecture_length:
        if lecture > bluray_size:
            return False
        else:
            if size_used + lecture <= bluray_size:
                size_used += lecture
            else:
                bluray_used += 1
                size_used = lecture
    
    if bluray_used <= bluray_count:
        return True
    else:
        return False


# 1. TO GET THE INPUT

lecture_count, bluray_count = map(int, sys.stdin.readline().split())
lecture_length = list(map(int, sys.stdin.readline().split()))


# 3. TO SOLVE THE PROBLEM

left = 0
right = sum(lecture_length)

while left + 1 < right:
    
    mid = (left + right) // 2
    result = check(mid)
    
    if result:
        right = mid
    else:
        left = mid

print(right)