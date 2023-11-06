'''
BOJ 14939 - K-String (https://www.acmicpc.net/problem/30463)

There are N strings of a length of 10. Each only consists of numbers.
K-String is a string consisting of K different numbers.
Determine the number of a pair of two strings of which the concatenation of two strings forms a K-String.
'''

import sys


# 1. A FUNCTION FOR BIT OPERATION

# A function to convert a string into a bit expression
# For example, 0011223457 will be converted to "0010111111"

def bitmask(string):
    key = 0
    for char in string:
        key |=  (1 << int(char))
    return key

# A function to count the number of 1 in a number

def count_one(num):
    count = 0
    while num != 0:
        if num % 2 == 1:
            count += 1
        num >>= 1
    return count


# 2. TO GET THE INPUT

word_count, target = map(int, sys.stdin.readline().split())

bitmask_count = [0 for num in range(1024)]

for word_input in range(word_count):
    word = sys.stdin.readline().strip()
    bitmask_count[bitmask(word)] += 1


# 3. TO SOLVE THE PROBLEM

ans = 0

for num1 in range(1, 1024):
    for num2 in range(num1 + 1, 1024):
        if count_one(num1 | num2) == target:
            ans += bitmask_count[num1] * bitmask_count[num2]

for num in range(1, 1024):
    if count_one(num) == target:
        ans += bitmask_count[num] * (bitmask_count[num] - 1) // 2

print(ans)
