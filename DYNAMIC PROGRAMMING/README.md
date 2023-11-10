# Dynamic Programming

Dynamic Programming (DP) is a method that utilizes existing answer for sub-problems to solve a problem.
Since DP is more about ideas than implementation, you need experience and mathematical intuition to solve such problems. 

*Sample Code*

For example, let's assume your goal is to get the 35th number of the Fibonacci sequence. One way to solve this is to use recursion.

```python
# Recursion

def fibonacci(x):

    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
```

However, it takes a massive amount of time since it repeatedly calls fibonacci(x). However, dynamic programming enables you to solve the problem way faster with the following code. The code does not have redundant operations that calculate the values you already know.

```python
# Dynammic Programming

fibonacci = [0, 1]

for x in range(2, 36):
    fibonacci.append(fibonacci[x-1] + fibonacci[x-2])
```

