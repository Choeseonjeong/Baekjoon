def solution(brown, yellow):
    num = brown + yellow
    for h in range(1,num+1):
        w = num//h
        if (w-2)*(h-2)==yellow:
            return [w,h]