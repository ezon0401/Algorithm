## Sieve of Eratosthenes

Sieve of Eratosthenes checks whether a given number is a prime or not in O(N log (log N)) time complexity.

*Sample Code*
```python
prime = [1 for i in range(N+1)]
prime[0], prime[1] = 0, 0

num = 2
while num <= int(N ** 0.5):
    if prime[num]:
        for multiple in range(num * 2, N+1, num):
            prime[multiple] = 0
    num += 1
```
