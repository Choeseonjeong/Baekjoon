def solution(a, b):
    answer=0
    for a,b in zip(a,b):
        answer+= a*b
    return answer