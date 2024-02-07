'''
BOJ 17425 - Divisor Sum (https://www.acmicpc.net/problem/17425)

Let f(x) be the sum of all divisors of x. Let g(x) = f(1) + ... + f(x). 
Answer queries: Print g(x) for given x.
'''

import sys


# 1. TO CALCULATE F(X)

f_value = [1 for num in range(10 ** 6 + 1)]
f_value[0] = 0

for num in range(2, 10 ** 6 + 1):
    for multiple in range(num, 10 ** 6 + 1, num):
        f_value[multiple] += num


# 2. PREFIX SUM TO CALCULATE G(X)

g_value = [f_value[num] for num in range(10 ** 6 + 1)]

for num in range(1, 10 ** 6 + 1):
    g_value[num] += g_value[num-1]


# 3. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())
for test in range(test_count):
    num = int(sys.stdin.readline())
    print(g_value[num])