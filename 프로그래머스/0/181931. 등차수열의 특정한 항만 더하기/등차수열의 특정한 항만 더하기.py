def solution(a, d, included):
    answer = 0
    for idx, flag in enumerate(included):
        if flag == True:
            answer += a+idx*d
    return answer