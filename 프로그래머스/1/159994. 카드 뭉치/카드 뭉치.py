def solution(cards1, cards2, goal):
    one, two = 0,0
    answer = []
    for word in goal:
        if one < len(cards1) and cards1[one] == word:
            one += 1
            answer.append(word)
        if two < len(cards2) and cards2[two] == word:
            two += 1
            answer.append(word)
    return "Yes" if len(answer) == len(goal) else "No"
        
            