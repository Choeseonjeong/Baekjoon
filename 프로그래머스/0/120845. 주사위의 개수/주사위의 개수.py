def solution(box, n):
    answer = 1
    box = [i//n for i in box]
    for i in box:
        answer*=i
    return answer