from collections import deque
def solution(maps):
    n,m = len(maps),len(maps[0])  
    def findXY(start,end):
        sx,sy,ex,ey = 0,0,0,0
        for y in range(n):
            for x in range(m):
                if maps[y][x] == start:
                    sx,sy = x,y
                elif maps[y][x] == end:
                    ex,ey = x,y
        return sx,sy,ex,ey

    def bfs(start,end):
        sx,sy,ex,ey = findXY(start,end)
        dist = [[-1]*m for _ in range(n)]
        
        queue = deque()
        queue.append((sx,sy))
        dist[sy][sx] = 0
        dx,dy = [-1,1,0,0],[0,0,-1,1]
        
        while queue:
            x,y = queue.popleft()
            if (x==ex) and (y==ey):
                return dist[y][x]
            
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if (0<=nx<m) and (0<=ny<n) and dist[ny][nx]==-1 and maps[ny][nx]!="X":
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((nx,ny))
        return -1
    
    first = bfs("S","L")
    second = bfs("L","E")
    if first == -1 or second == -1:
        return -1
    return first+second