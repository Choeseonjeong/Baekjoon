from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    answer = []
    
    def bfs(sx, sy):
        queue = deque()
        queue.append((sx, sy))
        visited[sy][sx] = True
        total = int(maps[sy][sx])
        
        dx, dy = [0,0,-1,1],[1,-1,0,0]
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<m and 0<=ny<n and maps[ny][nx]!="X" and not visited[ny][nx]:
                    visited[ny][nx] = True
                    total += int(maps[ny][nx])
                    queue.append((nx, ny))
        return total
    
    for y in range(n):
        for x in range(m):
            if maps[y][x] != "X" and not visited[y][x]:
                answer.append(bfs(x,y))
    
    return sorted(answer) if answer else [-1]
