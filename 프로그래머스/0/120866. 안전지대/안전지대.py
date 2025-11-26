def solution(board):
    m,n = len(board),len(board[0])
    dx=[-1,1,0,0,-1,-1,1,1] 
    dy=[0,0,-1,1,-1,1,-1,1]
    boom = []
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                boom.append((i,j))
    
    for x,y in boom:
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    count = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                count += 1
    return count