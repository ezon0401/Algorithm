'''
CF1898A - Milica and String (https://codeforces.com/problemset/problem/1898/A)

Milica has a string S of length N, consisting only of characters A and B.
In one operation, she can choose the first i characters of S and change them all to either 'A' or 'B'.
Determine the minimum number of operations required for S to contain exactly K instances of B. 
'''

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test_input in range(test_count):
    
    string_length, target = map(int, sys.stdin.readline().split())
    string = sys.stdin.readline().strip()
    
    
    # 2. TO SOLVE THE PROBLEM
    
    b_total = string.count("B")
    if b_total == target:
        print(0)
    else:
        print(1)
        if b_total < target:
            a_count = 0
            for index in range(string_length):
                if string[index] == "A":
                    a_count += 1
                    if a_count == target - b_total:
                        print(index + 1, "B")
                        break
        elif b_total > target:
            b_count = 0
            for index in range(string_length):
                if string[index] == "B":
                    b_count += 1
                    if b_count == b_total - target:
                        print(index + 1, "A")
                        break