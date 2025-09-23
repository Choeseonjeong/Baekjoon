from collections import deque

def solution(prices):
    prices = deque(prices)
    result = []
    
    while len(prices)!= 0:
        num = prices.popleft()
        time = 0
        for price in prices:
            time+=1
            if num > price :
                break
        result.append(time)
    return result