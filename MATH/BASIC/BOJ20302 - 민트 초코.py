'''
BOJ 20302 - Mint Chocolate (https://www.acmicpc.net/problem/20302)

Determine whether the result of the given expression is an integer or not.
'''

import sys


# 2. FACTORIZATION USING SIEVE OF ERATOSTHENES

factorized = [num for num in range(100001)]
divisors = [[] for num in range(100001)]

for divisor in range(2, int(100000 ** 0.5) + 1):
    if factorized[divisor] != 1:
        for multiple in range(divisor * 2, 100001, divisor):
            while factorized[multiple] % divisor == 0:
                factorized[multiple] //= divisor
                divisors[multiple].append(divisor)

for num in range(2, 100001):
    if factorized[num] != 1:
        divisors[num].append(factorized[num])


# 1. TO GET THE INPUT

num_count = int(sys.stdin.readline())
expression = list(sys.stdin.readline().strip().split())


# 3. TO SOLVE THE PROBLEM

count = [0 for num in range(100001)]

for index in range(0, len(expression), 2):
    
    num = abs(int(expression[index]))
    if num == 0:
        print("mint chocolate")
        sys.exit()
    
    if index == 0 or expression[index-1] == "*":
        for divisor in divisors[num]:
            count[divisor] += 1
    else:
        for divisor in divisors[num]:
            count[divisor] -= 1
    
ans = "mint chocolate"
for index in range(100001):
    if count[index] < 0:
        ans = "toothpaste"
        break
print(ans)