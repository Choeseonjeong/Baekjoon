def solution(order):
    cnt = 0
    arr = ["3","6","9"]
    for i in str(order):
        if i in arr:
            cnt+=1
    return cnt