def solution(a, b):
    answer = 0
    for i,j in zip(a,b):
        answer+=j*i
    return answer