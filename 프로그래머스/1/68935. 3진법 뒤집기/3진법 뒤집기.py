def solution(n):
    num = 3
    arr = []
    answer = 0
    while n > 0:
        arr.append(n%num)
        n = n//num
    reArr = arr[::-1]
    for idx in range(len(reArr)):
        if reArr[idx]!=0:
            answer+=(num**idx)*(reArr[idx])
    return answer