from collections import deque
def solution(board):
    n,m = len(board),len(board[0])
    
    def findXY(word):
        for y in range(n):
            for x in range(m):
                if board[y][x]==word:
                    return x,y
    
    sx,sy= findXY("R")
    ex,ey = findXY("G")
    
    dist = [[987654321]*m for _ in range(n)]
    dist[sy][sx] = 0
    
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    
    queue = deque()
    queue.append((sx,sy))
    
    while queue:
        x,y = queue.popleft()
        if (x==ex) and (y==ey):
            return dist[y][x]
        
        for i in range(4):
            nx,ny = x,y
            while (0<=nx+dx[i]<m) and (0<=ny+dy[i]<n) and board[ny+dy[i]][nx+dx[i]] != "D":
                nx+=dx[i]
                ny+=dy[i]
            if dist[ny][nx] > dist[y][x] + 1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((nx,ny))
    return -1
    
    