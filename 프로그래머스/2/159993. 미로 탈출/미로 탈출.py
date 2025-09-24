from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    def bfs(start, end):
        sx, sy = start
        ex, ey = end
        dist = [[-1]*m for _ in range(n)]
        q = deque([(sx, sy)])
        dist[sx][sy] = 0

        dx = (-1, 1, 0, 0)
        dy = (0, 0, -1, 1)

        while q:
            x, y = q.popleft()
            if (x, y) == (ex, ey):
                return dist[x][y]
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != 'X' and dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
        return -1

    S = L = E = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S': S = (i, j)
            elif maps[i][j] == 'L': L = (i, j)
            elif maps[i][j] == 'E': E = (i, j)

    to_lever = bfs(S, L)
    if to_lever == -1:
        return -1
    to_exit = bfs(L, E)
    if to_exit == -1:
        return -1
    return to_lever + to_exit
