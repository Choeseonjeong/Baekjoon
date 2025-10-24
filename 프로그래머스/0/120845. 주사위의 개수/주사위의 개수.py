def solution(box, n):
    arr = []
    num = 1
    for i in box:
        arr.append(i//n)   
    for i in arr:
        num *= i
    return num