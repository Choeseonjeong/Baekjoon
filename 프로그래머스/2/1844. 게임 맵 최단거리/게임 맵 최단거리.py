from collections import deque
def solution(maps):
    n,m = len(maps),len(maps[0])
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 1
    
    queue = deque()
    queue.append((0,0))
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if (0<=nx<m) and (0<=ny<n) and visited[ny][nx] == -1 and maps[ny][nx]==1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx,ny))
                
    answer = visited[n-1][m-1]
    if answer == -1:
        return -1
    else:
        return answer
        