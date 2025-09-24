import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    n,m = len(maps),len(maps[0])
    visited = [[False]*m for _ in range(n)]
    answer = []
    def dfs(i,j,visited,maps,n,m):
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        visited[i][j] = True
        num = int(maps[i][j])
        
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if (0<=x<n) and (0<=y<m) and not visited[x][y] and maps[x][y] != "X":
                num += dfs(x, y, visited, maps, n,m)
        return num
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                answer.append(dfs(i,j,visited,maps,n,m))
    if answer:
        return sorted(answer)
    else:
        return [-1]