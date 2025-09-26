def solution(clothes):
    closet = dict()
    for cloth,kind in clothes:
        if kind not in closet:
            closet[kind] = [cloth]
        else:
            closet[kind] += [cloth]
    answer = 1
    for key,val in closet.items():
        answer*=(len(val)+1)
    return answer-1