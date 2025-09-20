from collections import deque
def solution(maps):
    n,m = len(maps),len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    visited[0][0] = True
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if not (0<=nx<n and 0<=ny<m): continue
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx,ny))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
        
        
        
        
        
        