'''
BOJ 12416 - Trees (https://www.acmicpc.net/problem/12416)

There are N trees, each needs a support power of B.
It is possible to use 1 or 2 supports for each tree.
Given support powers of supports, determine the minimum support power to support all N trees. 
Print -1 if impossible.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test_num in range(1, test_count+1):
    
    tree_count, stick_type_count, power_need = map(int, sys.stdin.readline().split())
    sticks = {}
    for stick_type in range(stick_type_count):
        power, count = map(int, sys.stdin.readline().split())
        sticks[power] = count
    
    
    # 2. TO SOLVE THE PROBLEM
    
    tree_left = tree_count
    ans = 0
    
    for power in range(power_need, 40001):
        
        for stick_power in sticks:
            
            if stick_power == power:
                if sticks[stick_power] != 0:
                    count = min(tree_left, sticks[stick_power])
                    ans += power * count
                    tree_left -= count
                    sticks[stick_power] -= count
            else:
                if power - stick_power in sticks:
                    if stick_power == power - stick_power:
                        if sticks[stick_power] >= 2:
                            count = min(tree_left, sticks[stick_power] // 2)
                            ans += power * count
                            tree_left -= count
                            sticks[stick_power] -= 2 * count
                    else:
                        if sticks[stick_power] != 0 and sticks[power - stick_power] != 0:
                            count = min(tree_left, sticks[stick_power], sticks[power - stick_power])
                            ans += power * count
                            tree_left -= count
                            sticks[stick_power] -= count
                            sticks[power - stick_power] -= count
            
            if tree_left == 0:
                break
        if tree_left == 0:
            break

    if tree_left:
        ans = -1
    print("Case #{}: {}".format(test_num, ans))