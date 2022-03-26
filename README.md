# algo.py
All Algorithms in PythonPython

+ Travalsal 
  + [Breath First Search](#bfs-algorithm)

  + [Depth First Search](#dfs-algorithm)

# BFS algorithm
```python
import collections

def bfs(graph, root):
    print("Graph:", graph, "\nRoot:", root, "\n", end="Breadth First Traversal: ")
    visited, queue = {root}, collections.deque([root])

    while queue: # queue != null

        root = queue.popleft() # dequeue
        print(str(root), end=" ")

        for node in graph[ root ]: # check children
            if node not in visited: # enqueue the unvisited
                visited.add(node) 
                queue.append(node)

bfs(
    {
        0: [
            1,
            2
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

### DFS algorithm

```python
# DFS algorithm
def dfs(graph, root):
    visited=set()
    def DFS(root):
        # function for dfs 
        if root not in visited:
            print(root, end=" ")
            visited.add(root)
            for node in graph[ root ]:
                DFS(node)

    print("Graph:", graph, "\nRoot: ", root, end="\nDepth First Search: ")
    
    DFS(root)
    
dfs(
  {
    5 : [
      3, 
      7
    ],
    3 : [
      2,
      4
    ],
    7 : [
      8
    ],
    2 : [],
    4 : [
      8
    ],
    8 : []
  }, 
  5
)
```
