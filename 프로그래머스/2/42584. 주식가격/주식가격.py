from collections import deque

def solution(prices):
    queue = deque(prices)
    result = []
    
    while len(queue) != 0:
        time = 0
        x = queue.popleft()
        
        for num in queue:
            time += 1
            if x > num:
                break
        result.append(time)
    return result