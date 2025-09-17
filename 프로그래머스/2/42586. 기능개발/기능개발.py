import math
def solution(progresses, speeds):
    days = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    result = []
    count = 0
    current = days[0]
    
    for day in days:
        if current >= day:
            count+=1
        else:
            result.append(count)
            count = 1
            current = day
    result.append(count)
    return result