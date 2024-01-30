'''
BOJ 13977 - Binominal Coefficient and Queries (https://www.acmicpc.net/problem/13977)

For M queries, print nCk % (10 ** 9 + 7).
'''

import sys
mod = 10 ** 9 + 7


# 2. AN ARRAY FOR FACTORIAL

factorial_mod = [1]

for num in range(1, 4000001):
    factorial_mod.append(factorial_mod[-1] * num % mod)


# 1. TO GET THE INPUT

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    N, K = map(int, sys.stdin.readline().split())


    # 3. TO SOLVE THE PROBLEM
    # According to Fermat's little theorem, if P is a prime number and A is not a multiple of P, pow(A, P-2) is a modular inverse of A. 
    
    ans = factorial_mod[N] * pow(factorial_mod[N-K], mod-2, mod) * pow(factorial_mod[K], mod-2, mod) % mod
    print(ans)