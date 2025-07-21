def solution(n):
    num = 0
    for i in range(1,n+1):
        answer = 0
        for j in range(i,n+1):
            answer += j
            if answer == n:
                num+=1
            elif answer>n:
                break
    return num