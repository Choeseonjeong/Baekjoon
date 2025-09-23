def solution(tickets):
    answer = []
    visited = [False for _ in range(len(tickets))]
    
    def bfs(start, path): # path는 리스트 
        # 종료 조건
        if len(path)==len(tickets) + 1:
            answer.append(path)
            return 
        
        for idx, ticket in enumerate(tickets):
            if (ticket[0] == start) and (not visited[idx]):
                visited[idx] = True
                bfs(ticket[1],path+[ticket[1]])
                visited[idx] = False
                
    bfs("ICN", ["ICN"])
    answer.sort()
    
    return answer[0]