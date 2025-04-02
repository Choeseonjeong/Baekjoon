def solution(n):
    answer = 1
    while n>0:
        n = n//answer
        answer+=1
        if n==1:
            return answer-1
    return answer-2