def solution(clothes):
    closet = {}
    num = 1
    for cloth, kind in clothes:
        if kind in closet:
            closet[kind] += [cloth]
        else:
            closet[kind] = [cloth]
    for _,i in closet.items():
        num *= (len(i)+1)
    return num-1