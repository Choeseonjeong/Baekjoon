from collections import deque
def solution(begin, target, words):
    def differ(a,b):
        count = 0
        for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1
        return True if count==1 else False
    
    def bfs(begin,depth):
        queue = deque()
        queue.append([begin,depth])
        
        while queue:
            text,depth = queue.popleft()
            if text == target:
                return depth
            for i in range(len(words)):
                if differ(text,words[i]):
                    queue.append((words[i],depth+1))
    
    if target not in words:
        return 0
    return bfs(begin,0)