'''
BOJ 17087 - Hide and Seek 6 (https://www.acmicpc.net/problem/17087)

You are now at location S and can move to S+D or S-D after a second.
Given the locations of friends, calculate the maximum value of D so that you can find all the friends.
'''

import sys
from math import gcd


# 1. TO GET THE INPUT

friend_count, now_loc = map(int, sys.stdin.readline().split())
friend_loc = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = abs(friend_loc[0] - now_loc)
for index in range(1, friend_count):
    ans = gcd(ans, abs(friend_loc[index] - now_loc))
print(ans)