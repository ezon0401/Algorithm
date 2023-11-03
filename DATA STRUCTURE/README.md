# Overview

This repository aims to introduce basic data structures. 

## Stack

Stack is a LIFO (Last-In, First-Out) data structure. It pushes an element at the end and pops the last element in O(1) time complexity.

*Application*

* Stack is used to find whether a parenthesis string is valid or not.
    * We push "(" to stack when it comes and pop when ")" comes. 
    * "(" must exist in stack whenever ")" comes. 
    * After iterating the string, the stack must be empty.

*Sample Code*
```python
stack = [1, 2, 3, 4]

stack.append(5) # Add Last Element
five = stack.pop() # Remove Last Element
```

## Queue

Queue is a FIFO (First-In, First-Out) data structure. It adds an element at the end and removes the first element in O(1) time complexity.

*Sample Code*
```python
from collections import deque

queue = deque([1, 2, 3, 4])

queue.append(5) # Add Last Element
one = queue.popleft() # Remove First Element
```

## Deque

Deque is a combination of stack and queue. It can add and remove an element at both ends in O(1) time complexity.

*Sample Code*
```python
from collections import deque

deque_example = deque([1, 2, 3, 4])

deque_example.appendleft(0) # Add First Element
zero = deque_example.popleft() # Remove First Element
deque_example.append(5) # Add Last Element
deque_example.pop() # Remove Last Element
```

## Priority Queue

A priority queue is a data structure that can access an element with the lowest (or highest) priority value in O(1) time complexity. We can push or pop an element with the lowest (or highest) priority value in O(log n) time.

*Tip*

* Unlike other programming languages, Python does not support customized priority queues. We can only access the minimum value (or maximum value if values are stored as negative numbers).

*Sample Code*

```python
import heapq

priority_queue = [1, 3, 2, 5, 4]

heapq.heappush(priority_queue, 8) # Add Element
one = heapq.heappop(priority_queue) # Remove Element

two = heapq[0] # Access Element with the Minimum Value
```