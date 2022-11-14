# algo.py
All Algorithms in PythonPython

+ Travalsal 

  + [Breath First Search](#bfs-algorithm)

  + [Depth First Search](#dfs-algorithm)
  
  
+ [N Queen Problem using BackTracking](#N-Queen-Problem-using-BackTracking)

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

### N Queen Problem using BackTracking

```python
global N
N = int(input("Enter Dimension of board : ")) 

def printSolution(board):
  for i in range(N):
    for j in range(N):
      print (board[i][j],end=' ')
    print()

def isSafe(board, row, col):
  for i in range(col):
    if board[row][i] == 1:
      return False
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  for i, j in zip(range(row, N, 1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  return True

def solveNQUtil(board, col):
  if col >= N:
    return True
  for i in range(N):
    if isSafe(board, i, col):
      board[i][col] = 1
      if solveNQUtil(board, col + 1):
        return True
      board[i][col] = 0
  return False

def solveNQ():
  board=list()
  for i in range(N):
    board.append(list()) 
    for j in range(N):
      board[i].append(0)
  if not solveNQUtil(board, 0) :
    print ("Solution does not exist")
  printSolution(board)

solveNQ()
```
