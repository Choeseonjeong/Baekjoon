from collections import deque

def solution(cacheSize, cities):
    cash = deque()
    time = 0
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        city = city.lower()
        if city in cash:
            time += 1
            cash.remove(city)
            cash.append(city)
        else:
            if len(cash) < cacheSize:
                time += 5
                cash.append(city)
            else:
                time += 5
                cash.popleft()
                cash.append(city)
    return time