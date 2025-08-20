def solution(a, b):
    answer = 0
    n = str(a)+str(b)
    m = str(b)+str(a)
    return int(n) if n>=m else int(m)