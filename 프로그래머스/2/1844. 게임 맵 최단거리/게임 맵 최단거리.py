from collections import deque

def solution(maps):
    M,N = len(maps),len(maps[0])
    visited = [[-1]*N for _ in range(M)]
    dx,dy = (-1,1,0,0),(0,0,-1,1)
    
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<= nx < M and 0<= ny <N:
                if maps[nx][ny] ==1 and visited[nx][ny] ==-1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                
    return visited[M-1][N-1]
                
                
                
                