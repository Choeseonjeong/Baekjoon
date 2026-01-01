def solution(sides):
    m,n = max(sides),min(sides)
    answer = []
    for i in range(m-n+1,m+1):
        answer.append(i)
    for i in range(m+1,m+n):
        answer.append(i)
    return len(answer)