'''
BOJ 6588 - Goldbach's Conjecture (https://www.acmicpc.net/problem/6588)

Express a given even number to a sum of two prime numbers.  
'''


import sys


# 2. THE SIEVE OF ERATOSTHENES

prime = [1 for num in range(10 ** 6 + 1)]
prime[0], prime[1] = 0, 0

for num in range(2, int((10 ** 6 + 1) ** 0.5) + 1):
    if prime[num]:
        for multiple in range(num * 2, 10 ** 6 + 1, num):
            prime[multiple] = 0


# 1. TO GET THE INPUT

while True:
    
    target = int(sys.stdin.readline())
    if target == 0:
        break
    
    
    # 3. TO SOLVE THE PROBLEM
    
    possible = False
    for num in range(3, target // 2 + 1, 2):
        if prime[num] and prime[target - num]:
            possible = True
            break
    
    if possible:
        print("{} = {} + {}".format(target, num, target-num))
    else:
        print("Goldbach's conjecture is wrong.")