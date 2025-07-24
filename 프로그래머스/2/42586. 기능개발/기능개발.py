from math import ceil 

def solution(progresses, speeds):
    days = [ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    result = []
    
    max_day = days[0]
    count = 1
    
    for i in range(1,len(days)):
        if max_day >= days[i]: 
            count+=1
        else:
            result.append(count)
            max_day = days[i]
            count=1
    result.append(count)
    return result
            
            
            
            
            