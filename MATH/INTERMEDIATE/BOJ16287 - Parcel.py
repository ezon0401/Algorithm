'''
BOJ 16287 - Parcel (https://www.acmicpc.net/problem/16287)

Given an array, determine whether it is possible to choose 4 elements so that their sum equals K.
'''

import sys


# 2. A FUNCTION TO CHECK DUPLICATION

def duplication(arr1, arr2):
    
    for i1, j1 in arr1:
        for i2, j2 in arr2:
            if i1 != i2 and i1 != j2 and j1 != i2 and j1 != j2:
                return False
    
    return True


# 1. TO GET THE INPUT

target, arr_length = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 3. TO SOLVE THE PROBLEM

pair_sum = [[] for num in range(target+1)]

for i in range(arr_length):
    for j in range(i+1, arr_length):
        
        if arr[i] + arr[j] <= target and len(pair_sum[arr[i] + arr[j]]) < 3:
            pair_sum[arr[i] + arr[j]].append((arr[i], arr[j]))
    
ans = "NO"

for num in range(target // 2 + 1):
    
    if len(pair_sum[num]) != 0 and len(pair_sum[target-num]) != 0 and not duplication(pair_sum[num], pair_sum[target-num]):
        ans = "YES"
        break

print(ans)