def solution(k, m, score):
    answer=[]
    result=0
    arr = sorted(score,reverse=True)
    for i in range(0,len(score),m):
        answer.append(arr[i:i+m])   
    
    for i in answer:
        if len(i)==m:
            result+=i[-1]*m
    return result 
    
        