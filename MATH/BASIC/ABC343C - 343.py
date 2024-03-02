'''
ABC343C - 343 (https://atcoder.jp/contests/abc343/tasks/abc343_c)

Find the maximum value of a palindromic cubic number not greater than N.
'''

import sys


# 1. FIND PALINDROMIC CUBIC NUMBERS

def palindrome(num):

    num = str(num)

    for index in range(len(num) // 2):
        if num[index] != num[-index-1]:
            return False

    return True

palindromic_cubes = []
for num in range(10 ** 6 + 1):
    if palindrome(num ** 3):
        palindromic_cubes.append(num ** 3)


# 2. TO SOLVE THE PROBLEM

num = int(sys.stdin.readline())
ans = 0
for palindromic_cube in palindromic_cubes:
    if palindromic_cube <= num:
        ans = palindromic_cube
    else:
        break

print(ans)