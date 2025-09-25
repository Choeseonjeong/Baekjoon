from collections import deque

def solution(board):
    n,m = len(board),len(board[0])
    visited = [[987654321]* m for _ in range(n)]
    sx,sy = 0,0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                sx,sy = i,j
    visited[sx][sy] = 0
    
    queue = deque()
    queue.append((sx,sy,0))
    
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    while queue:
        x,y,depth = queue.popleft()
        
        if board[x][y] == "G":
            return depth
        
        for i in range(4):
            nx,ny = x,y
            while (0<=nx+dx[i]<n) and (0<=ny+dy[i]<m) and board[nx+dx[i]][ny+dy[i]] != "D":
                nx += dx[i]
                ny += dy[i]
                
            if visited[nx][ny] > depth + 1:
                visited[nx][ny] = depth + 1
                queue.append((nx,ny,depth+1))
    return -1
            
                
                
                
                
                
                
                
        