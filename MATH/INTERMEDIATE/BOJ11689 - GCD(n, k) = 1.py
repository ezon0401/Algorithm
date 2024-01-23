'''
BOJ 11689 - GCD(n, k) = 1 (https://www.acmicpc.net/problem/11689)

Given N, print the number of K that satisfies 1 <= K <= N and GCD(N, K) = 1.
'''

import sys
from itertools import combinations


# 3. A FUNCTION TO GET PRODUCT OF ELEMENTS IN A COMBINATION

def product(combination):
    
    result = 1
    for element in combination:
        result *= element
    
    return result
    

# 1. THE SIEVE OF ERATOSTHENES

prime = [1 for index in range(10 ** 6 + 1)]
prime[0], prime[1] = 0, 0

num = 2
while num <= 1000:
    if prime[num]:
        for multiple in range(2 * num, 10 **  6 + 1, num):
            prime[multiple] = 0
    num += 1


# 2. PRIME FACTORIZATION

N = int(sys.stdin.readline())

N_copy = N
prime_factor = []

for factor in range(2, int(N ** 0.5) + 1):
    if prime[factor] and N_copy % factor == 0:
        while N_copy % factor == 0:
            N_copy //= factor
        prime_factor.append(factor)

if N_copy != 1:
    prime_factor.append(N_copy)



# 4. TO SOLVE THE PROBLEM (INCLUSION-EXCLUSION PRINCIPLE)

num_with_common_factor = 0
plus = True

for element_num in range(1, len(prime_factor) + 1):
    
    for combination in combinations(prime_factor, element_num):
        
        if plus:
            num_with_common_factor += N // product(combination)
        else:
            num_with_common_factor -= N // product(combination)
    
    plus = not plus
    
print(N - num_with_common_factor)