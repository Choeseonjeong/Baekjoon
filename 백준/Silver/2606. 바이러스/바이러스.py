import sys
from collections import deque

# bfs 
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
net = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)



def bfs(): 
  q = deque()
  q.append(1)
  count = 0
  visited[1] = True
  
  while q:
    cur = q.popleft()
    for idx, val in enumerate(net[cur]):
      if not visited[val]:
        q.append(val)
        count += 1
        visited[val] = True
  print(count)
  
visited = [False for _ in range(N+1)]
bfs()





    
