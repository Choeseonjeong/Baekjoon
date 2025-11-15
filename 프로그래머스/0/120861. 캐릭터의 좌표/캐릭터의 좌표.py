def solution(keyinput, board):
    answer = {"up":[0,1],"down":[0,-1],"left":[-1,0],"right":[1,0]}
    max_x, max_y = board[0]//2, board[1]//2
    x,y = 0,0
    
    for word in keyinput:
        dx,dy = answer[word]
        if abs(dx+x) > max_x or abs(dy+y) > max_y:
            continue
        else:
            x,y = dx+x,dy+y
    return [x,y]