def solution(n, computers):
    def dfs(n,computers,com,visited):
        visited[com] = True
        for connect in range(len(computers[0])):
            if connect!=com and not visited[connect] and computers[com][connect] == 1:
                dfs(n,computers,connect,visited)
    
    visited = [False]*len(computers)
    answer = 0
    for com in range(len(computers)):
        if not visited[com]:
            dfs(n,computers,com,visited)
            answer+=1
    return answer