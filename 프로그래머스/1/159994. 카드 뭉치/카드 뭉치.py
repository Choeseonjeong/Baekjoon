def solution(cards1, cards2, goal):
    result=[]
    for i in goal:
        if cards1 and i == cards1[0]:
            result.append(i)
            cards1.remove(cards1[0])
        elif cards2 and i == cards2[0]:
            result.append(i)
            cards2.remove(cards2[0])
        else:
            return "No"
    if goal==result:
        return "Yes"
    else:
        return "No"