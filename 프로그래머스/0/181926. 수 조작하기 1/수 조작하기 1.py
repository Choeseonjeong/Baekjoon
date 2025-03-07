def solution(n, control):
    arr = { "w":1, "s":-1, "d":10, "a":-10 }
    answer = n
    for i in list(control):
        if i in arr.keys():
            answer += arr[i]
    return answer
            