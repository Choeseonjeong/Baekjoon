def solution(n):
    answer = 0
    def multi(x):
        count = 0
        for i in range(1,x+1):
            if x % i == 0:
                count+=1
        if count>=3:
            return 1
        else:
            return 0
    
    for x in range(1,n+1):
        answer+= multi(x)
    return answer
        
    