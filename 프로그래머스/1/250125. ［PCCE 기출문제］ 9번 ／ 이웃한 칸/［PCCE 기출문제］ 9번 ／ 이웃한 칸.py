def solution(board, h, w):
    count = 0
    num = len(board)
    dh = [-1,1,0,0]
    dw = [0,0,-1,1]
    for i in range(4):
        hx = dh[i] + h
        hy = dw[i] + w
        if 0 <= hx < num and 0 <= hy < num:
            if board[h][w]==board[hx][hy]:
                count+=1
    return count