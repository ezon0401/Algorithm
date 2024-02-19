'''
BOJ 31416 - Virtual Validation Technology (https://www.acmicpc.net/problem/31416)

There are a car A and a car B. There are also a junior researcher and a senior researcher.
For A and B, the number of tests and time required for each test are given.
Junior researcher can only test car A, while senior researcher can test both.
Determine the minimum time to complete all tests.
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    time_A, time_B, count_A, count_B = map(int, sys.stdin.readline().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    time_senior = time_B * count_B
    time_junior = 0
    
    while time_junior <= time_senior and count_A > 0:
        time_junior += time_A
        count_A -= 1
    
    if count_A > 0:
        if count_A % 2 == 0:
            time_senior += time_A * (count_A // 2)
            time_junior += time_A * (count_A // 2)
        else:
            time_senior += time_A * (count_A // 2 + 1)
            time_junior += time_A * (count_A // 2)
    
    print(max(time_junior, time_senior))