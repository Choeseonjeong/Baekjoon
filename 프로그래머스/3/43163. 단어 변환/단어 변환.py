from collections import deque

def solution(begin, target, words):
    def differ(a,b):
        count = 0
        for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1
        return True if count==1 else False
    
    def bfs(begin,target,words):
        queue = deque()
        queue.append([begin,0])
        
        while queue:
            text, depth = queue.popleft()
            if target==text:
                return depth
        
            for num in words:
                if differ(text,num):
                    queue.append((num,depth+1))
                    
    if target not in words:
        return 0
    return bfs(begin,target,words)