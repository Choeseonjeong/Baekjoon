def solution(clothes):
    closet = {}
    for cloth, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [cloth]
        else:
            closet[kind] = [cloth]
    answer = 1
    for cloth,kind in closet.items():
        answer *= (len(kind)+1)
    return answer -1