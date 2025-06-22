def solution(brown, yellow):
    num = brown + yellow
    answer = []
    
    for h in range(3,num+1):
        w = num//h
        if (w - 2) * (h - 2) == yellow:
            return [w, h]