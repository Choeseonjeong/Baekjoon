from collections import deque
def solution(maps):
    n,m = len(maps),len(maps[0]) # y,x
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        while queue: # 길이 끝나면 nx,ny는 큐에서 사라짐 
            # for이 한 블럭 
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 벽이면
                if maps[nx][ny]==0:
                    continue
                # 길이면
                if maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] + 1 
                    queue.append((nx,ny))
        if maps[n-1][m-1] == 1:
            return -1
        else:
            return maps[n-1][m-1]
    return bfs(0, 0)
            
            
            
            
            
    