import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def dfs(x, y) -> int:
    visited[x][y] = True
    count = 1
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if 0 <= nx < N and 0 <= ny < N:
            if grid[nx][ny]==1 and not visited[nx][ny]:
                count += dfs(nx,ny)
    return count

sizes = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            sizes.append(dfs(i, j))

sizes.sort()
print(len(sizes))
print(*sizes, sep="\n")