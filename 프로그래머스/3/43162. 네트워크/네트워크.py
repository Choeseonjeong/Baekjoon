def solution(n, computers):
    visited = [False]*n
    answer = 0
    
    def dfs(n,computers,com,visited):
        visited[com] = True
        for connect in range(n):
            if com!=connect and computers[com][connect]==1 and not visited[connect]:
                dfs(n,computers,connect,visited)
    
    for com in range(n):
        if not visited[com]:
            dfs(n,computers,com,visited)
            answer+=1
    return answer
    
    