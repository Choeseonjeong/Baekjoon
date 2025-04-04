def solution(arr, flag):
    answer = []
    for a, f in zip(arr, flag):
        if f: 
            answer.extend([a] * (a * 2))  
        else:  
            answer = answer[:-a] 
    return answer
