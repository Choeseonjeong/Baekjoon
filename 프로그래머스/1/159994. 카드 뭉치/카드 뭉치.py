def solution(cards1, cards2, goal):
    a, b, c = 0, 0, 0

    while c < len(goal):
        if a < len(cards1) and goal[c] == cards1[a]:
            a += 1
            c += 1
        elif b < len(cards2) and goal[c] == cards2[b]:
            b += 1
            c += 1
        else:
            return "No"
    
    return "Yes"
