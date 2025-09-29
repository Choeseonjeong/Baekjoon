def solution(absolutes, signs):
    answer = 0
    for num, flag in zip(absolutes, signs):
        if flag == True:
            answer+=num
        else:
            answer-=num
    return answer