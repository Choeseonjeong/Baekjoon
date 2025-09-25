import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    
    cur = days[0]
    count = 1
    for i in range(1,len(days)):
        if cur >= days[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            cur = days[i]
    answer.append(count)
    return answer