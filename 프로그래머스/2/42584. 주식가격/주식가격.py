from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []
    
    while queue:
        num = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if num > q:
                break
        answer.append(sec)
    return answer