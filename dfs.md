# DFS algorithm

```python
def dfs(visited=set(), graph, root):
    if root not in visited:
        print(root, end=" ")
        visited.add(root)
        for node in graph[root]:
            dfs(visited, graph, node)

graph = {
  5 : [3, 7],
  3 : [2,4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}

root = 5

print("Graph:", graph, "\nRoot: ", root, end="\nDepth First Search: ")

dfs(visited, graph, root)
```
