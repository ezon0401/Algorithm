'''
BOJ 30166 - Rainy day (https://www.acmicpc.net/problem/30166)

There are two buildings: A and B.
N students at A want to move to B without being soaked with rain.
Initially, there are M umbrellas of capacity K at building A.
What is the minimum number of moves?
'''

import sys


# 1. TO SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())
for test in range(test_count):
    
    student_count, umbrella_count, umbrella_capacity = map(int, sys.stdin.readline().split())
    
    if umbrella_count == 1 and umbrella_capacity == 1:
        if student_count == 1:
            print(1)
        else:
            print(-1)
    else:
        count = 1
        while student_count > umbrella_count * umbrella_capacity:
            count += 2
            student_count = student_count - umbrella_count * umbrella_capacity + 1
        print(count)
        