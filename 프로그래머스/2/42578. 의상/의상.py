def solution(clothes):
    closet = dict()
    for cloth,kind in clothes:
        if kind not in closet:
            closet[kind] = [cloth]
        else:
            closet[kind] += [cloth]
    answer = 1
    for i, j in closet.items():
        answer*=(len(j)+1)
    return answer-1