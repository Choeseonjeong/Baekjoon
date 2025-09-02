def solution(s):
    
    lenS = s.split(" ")
    for i in range(len(lenS)):
        lenS[i] = lenS[i].capitalize()
        answer = ' '.join(lenS)
    return answer