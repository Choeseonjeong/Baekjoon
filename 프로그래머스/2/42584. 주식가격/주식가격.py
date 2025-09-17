def solution(prices):
    result = [0 for _ in range(len(prices))]
    for idx, num in enumerate(prices): 
        time = 0
        for i in range(idx+1,len(prices)): 
            time+=1
            if num > prices[i]:
                break
        result[idx] = time
    return result