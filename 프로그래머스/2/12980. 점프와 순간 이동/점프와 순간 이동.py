def solution(n):
    num  = bin(n)
    cnt = 0
    for i in list(num):
        if i == '1':
            cnt +=1 
    return cnt
