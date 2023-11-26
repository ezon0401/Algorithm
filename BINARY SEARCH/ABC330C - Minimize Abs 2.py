'''
ABC330C - Minimize Abs 2 (https://atcoder.jp/contests/abc330/tasks/abc330_c)

A positive number D is given.
Find the minimum value of abs(x ^ 2 + y ^ 2 - D) for non-negative integers x and y.
'''

import sys
from bisect import bisect_left


# 1. TO GET INPUT

target = int(sys.stdin.readline())


# 2. TO GET SQUARE NUMBERS

square_nums = [0]
for num in range(1, int(target ** (0.5)) + 1):
    square_nums.append(num ** 2)


# 3. TO SOLVE THE PROBLEM

ans = float('inf')
for square_num in square_nums:
    
    key = target - square_num
    
    index = bisect_left(square_nums, key)
    if index != len(square_nums):
        ans = min(ans, abs(key - square_nums[index]))
    if index != 0:
        ans = min(ans, abs(key - square_nums[index-1]))
        
print(ans)