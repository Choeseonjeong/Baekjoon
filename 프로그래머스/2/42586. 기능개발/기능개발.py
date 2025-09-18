import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(speeds))]
    
    one = days[0]
    result = []
    count = 1
    
    for i in range(1,len(days)):
        if one >= days[i]:
            count+=1
        else:
            one = days[i]
            result.append(count)
            count = 1
    result.append(count)
    return result
            
        