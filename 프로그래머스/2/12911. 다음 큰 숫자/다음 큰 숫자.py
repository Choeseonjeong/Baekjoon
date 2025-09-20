def solution(n):
    num = bin(n)[2:].count("1")
    b = n
    while True:
        b+=1
        b_num = bin(b)[2:].count("1")
        if num == b_num:
            return b