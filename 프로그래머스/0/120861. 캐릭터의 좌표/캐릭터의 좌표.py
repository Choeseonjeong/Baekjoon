def solution(keyinput, board):
    dir = {'up' : [0, 1], 'down' : [0, -1], 'left' : [-1, 0], 'right' : [1, 0]}
    x,y = 0,0
    m,n = board[0]//2,board[1]//2
    for key in keyinput:
        dx,dy = dir[key]
        nx,ny = x+dx,y+dy
        if -m <= nx <= m and -n <= ny <= n:
            x, y = nx, ny   
    return x,y