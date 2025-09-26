from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 102
    maps = [[0]*MAX for _ in range(MAX)]
    dist = [[-1]*MAX for _ in range(MAX)]
    for sx, sy, ex, ey in rectangle:
        sx, sy, ex, ey = sx*2, sy*2, ex*2, ey*2
        for y in range(sy, ey+1):
            for x in range(sx, ex+1):
                maps[y][x] = 1

    for sx, sy, ex, ey in rectangle:
        sx, sy, ex, ey = sx*2, sy*2, ex*2, ey*2
        for y in range(sy+1, ey):
            for x in range(sx+1, ex):
                maps[y][x] = 0

    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    # maps = 길인지 확인, dist = 숫자 더하기 
    queue = deque()
    queue.append((characterX, characterY))
    dist[characterY][characterX] = 0
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        if (x==itemX) and (y==itemY):
            return dist[itemY][itemX]//2
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<MAX) and (0<=ny<MAX) and maps[ny][nx]==1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((nx,ny))
    return -1
            