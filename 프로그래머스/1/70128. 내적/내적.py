def solution(a, b):
    num = 0
    for i,j in zip(a,b):
        num+=j*i
    return num