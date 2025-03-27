def solution(n):
    num = n**0.5
    if int(num)==num:
        return (num+1)*(num+1)
    else:
        return -1