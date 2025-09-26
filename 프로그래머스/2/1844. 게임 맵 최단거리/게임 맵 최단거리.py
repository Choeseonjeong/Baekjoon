from collections import deque
def solution(maps):
    n,m = len(maps),len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    dx,dy = [0,0,-1,1],[-1,1,0,0]
    
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if (0<=nx<m) and (0<=ny<n) and visited[ny][nx] == -1 and maps[ny][nx]==1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx,ny))
            else:
                continue
    return visited[n-1][m-1]
        