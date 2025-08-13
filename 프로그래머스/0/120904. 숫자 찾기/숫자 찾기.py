def solution(num, k):
    num = list(str(num))
    if str(k) in num:
        return num.index(str(k))+1
    return -1