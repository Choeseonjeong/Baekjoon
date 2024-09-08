def solution(n):
    str_n = str(n)
    a = 0
    for i in str_n:
        a += int(i)
    return a
