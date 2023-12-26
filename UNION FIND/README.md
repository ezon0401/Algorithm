# Union Find

Union-find is an algorithm for the disjoint set data structure. Disjoint set is a group of sets with no common elements.

The union-find algorithm consists of two main functions. The function find() returns the set an element belongs to, and the function union() combines two sets.

## Sample Code

```python
parent = [element_num for element_num in range(element_count)]

def find(element):

    if element_num != parent[element_num]:
        parent[element_num] = find(parent[element_num])
    return parent[element_num]

def union(elementA, elementB):

    parentA = find(elementA)
    parentB = find(elementB)

    if parentA < parentB:
        parent[parentA] = parentB
    else:
        parent[parentB] = parentA
```