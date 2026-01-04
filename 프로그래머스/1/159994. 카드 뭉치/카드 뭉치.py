def solution(cards1, cards2, goal):
    answer = ''
    a,b = 0,0
    for ch in goal:
        if a < len(cards1) and cards1[a] == ch:
            a += 1
        elif b < len(cards2) and cards2[b] == ch:
            b += 1
        else:
            return "No"
    return 'Yes'