# DFS and BFS

Depth First Search (DFS) and Breadth First Search (BFS) are well-known O(V+E) graph search algorithms.

Let's assume there exists the following graph. If one can visit multiple vertices, we will follow the alphabetical order.

```
A - B - D - E - F
    |   |   |
    C   G - H
```

Names are straightforward.

DFS prioritizes depth, that is, to visit deeper vertices if possible. In other words, it searches a possible path until it ends, then moves to another. The order of visits would be A-B-C-D-E-F-H-G for the graph above. 

Meanwhile, BFS prioritizes breadth. From the starting point, it searches each possible path little by little. The order of visits would be A-B-C-D-E-G-F-H for the graph above. 

## Application

* If all edges in the graph have the same length, the BFS path from vertex A to vertex B is the shortest path from vertex A to vertex B. 

    However, the DFS path may not be the shortest. In the graph above, the shortest path from the vertex A to the vertex G would be A-B-D-G, but the DFS path returns A-B-D-E-H-G.

## Sample Code

*DFS*

```python
def dfs(start_vertex):
    for next_vertex in graph[start_vertex]:
        if visited[next_vertex] == 0:
            visited[next_vertex] = 1
            dfs(next_vertex)
```

*BFS*
```python
bfs = deque([start_vertex])
visited[start_vertex] = 1
while bfs:
    now_vertex = bfs.popleft()
    for next_vertex in graph[now_vertex]:
        if visited[next_vertex] == 0:
            visited[next_vertex] = 1
            bfs.append(next_vertex)
```

*Tip*

1. Never forget to check whether a vertex is visited or not. Otherwise, the program will execute tremendous amounts of redundant operations.
2. The dy and dx arrays, which indicate how to move to the next vertices, can simplify the code.
3. If you use Python, the recursion limit may be insufficient. If necessary, change the limit using ```sys.setrecursionlimit()```.