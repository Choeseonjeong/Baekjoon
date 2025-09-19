from collections import deque

def solution(begin, target, words):
    def differ(a,b):
        count = 0
        for i,j in zip(a,b):
            if i!=j:
                count+=1
        if count == 1:
            return True
        return False
    
    queue = deque([(begin, 0)])
    visited = [False]*len(words)
    
    while queue:
        text, depth = queue.popleft()
        if text == target:
            return depth 
        for idx, word in enumerate(words):
            if not visited[idx] and differ(text,words[idx]):
                visited[idx] = True
                queue.append((words[idx], depth + 1))
    return 0