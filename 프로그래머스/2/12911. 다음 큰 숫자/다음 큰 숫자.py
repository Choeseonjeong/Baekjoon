def solution(n):
    num = n # 79
    ncnt = bin(n)[2:].count("1")
    cnt = 0
    
    while True:
        if ncnt == cnt:
            break
        num+=1
        cnt = bin(num)[2:].count("1")
    return num