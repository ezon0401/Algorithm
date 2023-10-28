'''
ABC326C - Peak (https://atcoder.jp/contests/abc326/tasks/abc326_c)

There are N gifts on a number line.
You can choose a half-open interval [x, x+M) to acquire all the gifts included in it.
What is the maximum number of gifts you can get?
'''

import sys
from bisect import bisect_left


# 1. TO GET THE INPUT

gift_count, interval_size = map(int, sys.stdin.readline().split())
gifts_loc = list(map(int, sys.stdin.readline().split()))

gifts_loc.sort()


# 2. TO SOLVE THE PROBLEM

ans = 0

for interval_start in range(gift_count):
    interval_end = bisect_left(gifts_loc, gifts_loc[interval_start] + interval_size)
    ans = max(ans, interval_end - interval_start)

print(ans)