# Prefix Sum

Prefix sum is a technique that facilitates partial sum calculation.

*Sample Code*

For example, let's assume an array [1, 8, 7, 3, 2, 9, 12, 30, 2, 1].
The goal is to get partial sum from index 4 to index 8.
Indeed, it is possible to achieve the goal without using prefix sum technique.

```python
arr = [1, 8, 7, 3, 2, 9, 12, 30, 2, 1]

partial_sum = 0
for index in range(4, 9):
    partial_sum += arr[index]

print(partial_sum)
```

However, its time complexity is O(N). Using the prefix sum technique, we can make it O(1). The idea is to use a prefix_sum array that stores prefix sum.

```python
arr = [1, 8, 7, 3, 2, 9, 12, 30, 2, 1]

prefix_sum = []
for num in arr:
    if len(prefix_sum) == 0:
        prefix_sum.append(num)
    else:
        prefix_sum.append(prefix_sum[-1] + num)

print(prefix_sum[8] - prefix_sum[3])
```

The difference in efficiency gets more visible as the array gets large and the number of queries increases. 
