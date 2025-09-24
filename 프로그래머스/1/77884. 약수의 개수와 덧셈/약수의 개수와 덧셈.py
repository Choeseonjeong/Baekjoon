def solution(left, right):
    def isprime(num):
        count = 0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        return count
    answer = 0
    for idx in range(left,right+1):
        if isprime(idx)%2==0:
            answer+=idx
        else:
            answer-=idx
    return answer
    
            