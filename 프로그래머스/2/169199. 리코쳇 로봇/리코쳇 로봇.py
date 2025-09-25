from collections import deque
def solution(board):
    n,m = len(board),len(board[0])
    sx,sy,ex,ey = 0,0,0,0
    for y in range(n):
        for x in range(m):
            if board[y][x] == "R":
                sx,sy = x,y
            elif board[y][x] == "G":
                ex,ey = x,y
    visited = [[987654321] * m for _ in range(n)]

    queue = deque()
    queue.append((sx,sy,0))
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    visited[sy][sx] = 0
    
    while queue:
        x,y,depth = queue.popleft()
        if (x==ex) and (y==ey):
            return depth
        for i in range(4):
            nx,ny = x,y
            while (0<=nx+dx[i]<m) and (0<=ny+dy[i]<n) and board[ny+dy[i]][nx+dx[i]] != "D":
                nx+=dx[i]
                ny+=dy[i]
            if visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx,ny,depth+1))
    return -1
            
            
            
            
            
            
            
            
            
            
            
            
        