def solution(n):
    num = 0
    while n!= 1:
        
        if num>=500:
            return -1
        if n%2==0:
            n/=2
        else:
            n = (n*3)+1
        num+=1
    return num