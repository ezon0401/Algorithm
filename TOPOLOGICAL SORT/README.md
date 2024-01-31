# Topological Sort

When you play a game, sometimes you can buy an item only after you buy other items. Similarly, some courses require prerequisite courses to take.

Directed acyclic graphs can represent such structures, and topological sort algorithm determines the order to access in O(V+E) time complexity.

It repeats two steps: (1) Access a vertex with in-degree of 0. (2) Delete all edges connected to the vertex. 

## Application

- If a graph contains a cycle, there must be a vertex that cannot have an in-degree of 1. Thus, if one or more vertex are not accessed during the topological sort, then the graph is cyclic.  

## Sample Code

```python
t_sort = deque([])
for index in range(vertex_count):
    if in_degree[index] == 0:
        t_sort.append(index)

order = []
while t_sort:
    now_vertex = t_sort.popleft()
    for next_vertex in graph[now_vertex]:
        in_degree[next_vertex] -= 1
        if in_degree[next_vertex] == 0:
            t_sort.append(next_vertex)
    order.append(now_vertex)
```