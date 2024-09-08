def solution(absolutes, signs):
    answer=0
    for absolutes, signs in zip(absolutes, signs):
        if signs==False:
            answer-=absolutes
        else:
            answer+=absolutes
    return answer