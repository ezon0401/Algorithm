'''
BOJ 3079 - Immigration (https://www.acmicpc.net/problem/3079)

There are N immigration desks and M arrivals.
The times each immigration desk take to examine an arrival are given.
Determine the minimum time to examine all M arrivals.
'''

import sys


# 2. A FUNCTION TO CHECK WHETHER A GIVEN TIME IS ENOUGH

def check(time):
    
    finish_count = 0
    for entry_check_time in check_time:
        finish_count += time // entry_check_time
    
    if finish_count >= friend_count:
        return True
    else:
        return False


# 1. TO GET THE INPUT

entry_count, friend_count = map(int, sys.stdin.readline().split())

check_time = []
for entry in range(entry_count):
    entry_check_time = int(sys.stdin.readline())
    check_time.append(entry_check_time)
    

# 3. TO SOLVE THE PROBLEM

left = 0
right = 10 ** 18

while left + 1 < right:
    
    mid = (left + right) // 2
    
    if check(mid):
        right = mid
    else:
        left = mid
        
print(right)