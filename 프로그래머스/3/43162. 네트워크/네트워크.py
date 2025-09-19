def solution(n, computers):
    
    def DFS(n,computers,computer,visited):
        visited[computer] = True
        for connect in range(n):
            if connect != computer and computers[computer][connect] == 1:
                if visited[connect]==False:
                    DFS(n,computers,connect,visited)
                
    answer = 0
    visited = [False]*n
    for computer in range(n):
        if visited[computer] == False:
            DFS(n,computers,computer,visited)
            answer+=1
    return answer
    
    
    
    