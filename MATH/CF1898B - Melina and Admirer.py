'''
CF1898B - Melina and Admirer (https://codeforces.com/problemset/problem/1898/B)

Melina has an array of integers of length N.
In one operation, she can choose an element X and replace it with two positive integers P and Q if P + Q = X.
Determine the minimum number of times of operation to make the array non-decreasing.
'''

import sys


# 2. A FUNCTION TO GET MATH.CEIL(X / Y)

def ceil(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())
for test_input in range(test_count):
    
    arr_length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 3. TO SOLVE THE PROBLEM
    # From the rightmost end, arr[index] must be divided if arr[index] > arr[index + 1]. 
    # The optimal way is to divide arr[index] as equally as possible.
    
    count = 0
    
    target = arr[-1]
    for index in range(arr_length - 2, -1, -1):
        if arr[index] <= target:
            target = arr[index]
        else:
            chunk = ceil(arr[index], target)
            count += chunk - 1
            target = arr[index] // chunk
    
    print(count)