def solution(n, computers):
    
    def dfs(n,computers,com,visited):
        visited[com] = True
        for connect in range(n):
            if computers[com][connect] == 1 and not visited[connect]:
                dfs(n,computers,connect,visited)
        
    visited = [False for _ in range(len(computers))]
    answer = 0
    for com in range(n):
        if visited[com] == False:
            dfs(n,computers,com,visited)
            answer += 1
    return answer