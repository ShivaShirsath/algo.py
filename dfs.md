# DFS algorithm

```python
# DFS algorithm
def dfs(graph, root):
    visited=set()
    def DFS(root):
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
