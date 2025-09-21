from collections import deque

def solution(cacheSize, cities):
    queue = deque(maxlen=cacheSize) 
    hit = 0
    cities = [i.lower() for i in cities]
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        if city in queue:
            queue.remove(city)
            queue.appendleft(city)
            hit += 1
        else:
            queue.appendleft(city)
            hit += 5
    return hit
