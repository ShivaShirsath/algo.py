# BFS algorithm in Python

```python
import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = {root}, collections.deque([root])

    while queue: # while queue is not empty

        key = queue.popleft() # dequeue
        print(str(key), end=" ")

        for value in graph[ key ]: # check children
            if value not in visited: # enqueue the unvisited
                visited.add(value) 
                queue.append(value)


if __name__ == '__main__':
    print("Following is Breadth First Traversal: ")
    bfs(
        {
            0: [
                1, 
                2, 
                3
            ], 
            1: [
                2, 
                1,
                3
            ],
            2: [
                3
            ], 
            3: [
                1,
                2
            ]
        }, 
        0
    )
```
