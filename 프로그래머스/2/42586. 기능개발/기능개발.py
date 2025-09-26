import math
def solution(progresses, speeds):
    days = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    
    result = []
    idx = 0
    
    for i in range(1,len(days)):
        if days[idx] < days[i]:
            result.append(i-idx)
            idx = i
    result.append(i-idx+1)
    return result