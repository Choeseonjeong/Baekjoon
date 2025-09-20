def solution(clothes):
    closet = {}
    for value,key in clothes:
        if key not in closet:
            closet[key] = [value]
        else:
            closet[key] += [value]
    answer = []
    num = 1
    for i,j in closet.items():
        answer.append(len(j))
    if len(answer)==1:
        return answer[0]
    else:
        for i in answer:
            num*=(i+1)
    return num-1