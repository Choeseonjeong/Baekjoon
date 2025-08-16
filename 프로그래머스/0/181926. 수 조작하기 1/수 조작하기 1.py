def solution(n, control):
    answer = n
    arr = {"w":1,"s":-1,"d":10,"a":-10}
    for i in control:
        answer+=arr[i]
    return answer