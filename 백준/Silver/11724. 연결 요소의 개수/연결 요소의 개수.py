# BOJ 11724 - 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
visited = [False] * (N + 1)

# === TODO: DFS 또는 BFS 구현 ===
def DFS(x):
    visited[x]=True
    for v in g[x]:
        if not visited[v]:
            DFS(v)
            
count = 0
for i in range(1,N+1):
    if visited[i] == False:
        DFS(i)
        count+=1
print(count)


