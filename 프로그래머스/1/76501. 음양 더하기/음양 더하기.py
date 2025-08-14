def solution(absolutes, signs):
    answer = 0
    for num,key in zip(absolutes, signs):
        if key == True:
            answer+=num
        else:
            answer-=num
    return answer