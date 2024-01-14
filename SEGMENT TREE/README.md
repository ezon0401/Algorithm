# Segment Tree

A segment tree is a data structure that can process specific kinds of queries faster.

Consider there is an array A = [1, 5, 2, 9, 3, 5, 6, 1], and we have to perform two kinds of queries: [A] Get the local sum from index a to index b / [B] Change k-th element to X. 

One way to implement this is to use the prefix sum. If we use the prefix sum, query A will take O(1), but query B will take O(N). Another way is to use an array. Then, query B will take O(1), but query A will take O(N).

Segment tree allows you to process both queries in O(log N) time complexity. 

The key idea is to store a local sum for each segment like the following image:

<p align="center">
    <img
        src = ".\img\Segment Tree.png"
        width = "360"
        height = "220"
    />
</p>

## Sample Code - Local Sum

```python 
arr = [1, 5, 2, 9, 3, 5, 6, 1]

# Query A - Local Sum
def local_sum(start, end):
    
    start += align 
    end += align

    result = 0
    while start <= end:
        if start % 2 == 1:
            result += seg_tree[start]
            start += 1
        if end % 2 == 0:
            result += seg_tree[end]
            end -= 1
        start >>= 1
        end >>= 1
    
    return result

# Query B - Change an element
def change(index, val):

    index += align
    change_val = val - seg_tree[index]
    while index != 0:
        seg_tree[index] += change_val
        index >>= 1

# To construct a segment tree
seg_tree = [0 for index in range(1 << 4)]

align = 1 << 3
for index in range(len(arr)):
    seg_tree[align + index] = arr[index]
for index in range(align-1, 0, -1):
    seg_tree[index] = seg_tree[index << 1] + seg_tree[(index << 1) | 1]
```