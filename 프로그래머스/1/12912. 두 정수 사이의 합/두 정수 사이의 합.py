def solution(a, b):
    answer = 0
    return sum([i for i in range(a,b+1)]) if a<b else sum([i for i in range(b,a+1)])