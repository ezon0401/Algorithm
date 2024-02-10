'''
BOJ 10819 - Max Difference (https://www.acmicpc.net/problem/10819)

There is an array A.
If it is possible to rearrange A, determine the maximum value of |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|. 
'''


import sys
from itertools import permutations


# 1. TO GET THE INPUT

num_count = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = 0
for permutation in permutations(arr, num_count):
    case_result = 0
    for index in range(1, num_count):
        case_result += abs(permutation[index-1] - permutation[index])
    ans = max(ans, case_result)

print(ans)