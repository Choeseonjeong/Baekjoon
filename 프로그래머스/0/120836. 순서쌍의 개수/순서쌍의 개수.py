def solution(n):
    answer = 0
    arr = [i for i in range(1,n+1)]
    for i in arr:
        if n%i==0:
            answer+=1
    return answer