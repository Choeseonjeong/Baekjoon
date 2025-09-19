# BOJ 1012 유기농 배추
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input().strip())
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    visited = [[False]*M for _ in range(N)]

    def in_range(r, c):
        return 0 <= r < N and 0 <= c < M
    
    def DFS(x,y):
        visited[x][y] = True
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if in_range(nx, ny) and field[nx][ny] == 1 and not visited[nx][ny]:
                DFS(nx,ny)    
    answer = 0
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1 and not visited[i][j]:
                DFS(i,j)
                answer+=1
    print(answer)
    
    