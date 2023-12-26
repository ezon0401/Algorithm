# Shortest Path

This repository introduces algorithms to get the shortest path. 

## Dijkstra

Dijkstra algorithm provides the shortest path if there are no edges of negative length. The time complexity is O(E log V).

The algorithm repeats two steps: (1) To choose the closest vertex and (2) to perform edge relaxation. Following is the example.

<p align="center">
    <img
        src = ".\img\example.png"
        width = "250"
        height = "200"
    />
</p>

Let's assume we start from vertex A. We choose vertex A and calculate the distance to adjacent vertices. Vertex B is now a distance of 1 and vertex C is a distance of 6. 

Now, the closest vertex that has not been chosen is vertex B. Thus, we choose vertex B. Again, we calculate the distance to adjacent vertices. Vertices C was originally a distance of 6, however, now it is a distance of 5. 

*Sample Code*
```python
import heapq

def dijkstra(start):
    
    visited = [float('inf') for v in range(vertex_count + 1)]

    heap = [(0, start)]
    visited[start] = 0
    while heap:
        now_dis, now_vertex = heapq.heappop(heap)
        if now_dis <= visited[now_vertex]:
            for next_dis, next_vertex in graph[now_vertex]:
                dis = now_dis + next_dis
                if dis < visited[next_vertex]:
                    visited[next_vertex] = dis
                    heapq.heappush(heap, (dis, next_vertex))
    
    return visited
```

## Bellman-Ford

What if there is an edge of negative length? If there is a cycle of negative length, the Dijkstra algorithm will never terminate. 

The idea of Bellman-Ford algorithm is that the number of edges of the shortest path is at most V-1. It updates the shortest path at most V-1 times. The time complexity is O(EV).

*Application*

* If a distance is updated at the V-th update, the graph contains a negative cycle.

*Sample Code*
```python
dist = [float('inf') for v in range(vertex_count + 1)]
dist[start] = 0
cycle = False

for update in range(1, vertex_count + 1):
    for now_vertex, next_vertex, distance in edge:
        if dist[now_vertex] + distance < dist[next_vertex]:
            if update == vertex_count:
                cycle = True
            dist[next_vertex] = dist[now_vertex] + distance
```

## Floyd-Warshall

Dijkstra algorithm or Bellman-Ford algorithm calculates the shortest path from one vertex to the others. Floyd-Warshall algorithm calculates the shortest path from vertex u to vertex v for arbitrary pair (u, v). The time complexity is O(V ^ 3).

The idea is simple. If i -> k -> j is shorter than i -> j, we update the path.

*Application*

* If you do not initialize a distance of loops to 0, you can get the shortest distance of a cycle.

*Sample Code*
```python
for vertex in range(V):
    graph[vertex][vertex] = 0

for k in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
```
