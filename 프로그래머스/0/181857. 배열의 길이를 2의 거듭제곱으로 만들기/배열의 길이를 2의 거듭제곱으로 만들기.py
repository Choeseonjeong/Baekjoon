# 2,4,8

def solution(arr):
    count = 0
    num = len(arr)
    while num>1:
        num=num/2
        count+=1
    return arr + [0] * (2 ** count - len(arr))
