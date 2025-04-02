def solution(n):
    result = []
    for num in range(1,n+1):
        if n%num==0:
            result.append(num)
    return result