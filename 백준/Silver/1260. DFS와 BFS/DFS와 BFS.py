import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())

# 행렬 만들기
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)  # dfs의 방문기록
visited2 = [False] * (N + 1)  # bfs의 방문기록


# dfs 
def dfs(V):
  visited1[V] = True
  print(V, end = ' ')
  for i in range(1,N+1):
    if not visited1[i] and graph[V][i]:
      dfs(i)
        
  
# bfs
def bfs(V):
  queue = deque([V])
  visited2[V] = True 
  while queue:
    V = queue.popleft()
    print(V,end=' ')
    for i in range(1,N+1):
      if not visited2[i] and graph[V][i]:
        queue.append(i)
        visited2[i] = True

dfs(V)
print()
bfs(V)
