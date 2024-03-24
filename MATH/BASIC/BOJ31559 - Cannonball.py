'''
BOJ 31559 - Cannonball (https://www.acmicpc.net/problem/31559)

There is a number line of length N.
Bessie starts at some location S and bounces the cannonball with a starting power of 1.
If the power is k, the next bounce will be at distant k.

Every integer location is either a target or a jump pad.
If the cannonball bounces off a jump pad with a value of v, the power increases by v and the direction will be reversed.
If the cannonball bounces off a target with a value lower than the power, the target will be broken.

Given S, print the number of targets Bessie will break. 
'''


import sys


# 1. TO GET THE INPUT

line_length, now = list(map(int, sys.stdin.readline().split()))
now -= 1

broken = [0 for loc in range(line_length)]
target = [0 for loc in range(line_length)]
value = [0 for loc in range(line_length)]

for loc in range(line_length):
    
    loc_target, loc_value = map(int, sys.stdin.readline().split())
    target[loc] = loc_target
    value[loc] = loc_value


# 2. TO SOLVE THE PROBLEM

power = 1
direction = 1
count = 0

# The number of bounce cannot be more than 10 ** 6.

while 0 <= now < line_length and count <= 10 ** 6:
    
    if target[now] == 0:
        power += value[now]
        direction *= -1
    else:
        if value[now] <= power:
            broken[now] = 1
        
    now += power * direction
    count += 1
    
ans = 0
for loc in range(line_length):
    if target[loc] and broken[loc]:
        ans += 1
print(ans)