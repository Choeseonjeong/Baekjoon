from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY): 
    x1,y1,x2,y2 = 0,0,0,0
    n,m = len(rectangle),len(rectangle[0])
    maxSize = 102
    maps = [[0]*maxSize for _ in range(maxSize)]
    dist = [[-1]*maxSize for _ in range(maxSize)]
    for x1,y1,x2,y2 in rectangle:
        x1,y1,x2,y2 = x1*2,y1*2,x2*2,y2*2
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                maps[y][x] = 1
    for x1,y1,x2,y2 in rectangle:
        x1,y1,x2,y2 = x1*2,y1*2,x2*2,y2*2
        for x in range(x1+1,x2):
            for y in range(y1+1,y2):
                maps[y][x] = 0
            
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    dist[characterY][characterX] = 0
    queue = deque()
    queue.append((characterX,characterY))
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        if (x==itemX) and (y==itemY):
            return dist[y][x]//2
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<maxSize) and (0<=ny<maxSize) and maps[ny][nx] == 1 and dist[ny][nx] ==-1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((nx,ny))
    return -1
    
    
    
    