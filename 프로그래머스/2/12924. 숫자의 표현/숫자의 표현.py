def solution(n):
    answer = 0
    for i in range(1,n+1):
        num = i
        if i == n:
            answer+=1
        for j in range(i+1,n+1):
            num+=j 
            if num > n:
                break
            elif num == n:
                answer+=1
                break
    return answer