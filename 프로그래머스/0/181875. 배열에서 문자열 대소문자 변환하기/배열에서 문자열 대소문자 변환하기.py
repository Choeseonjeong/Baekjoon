def solution(strArr):
    answer = []
    for idx, ch in enumerate(strArr):
        if idx%2==1:
            answer.append(ch.upper())
        else:
            answer.append(ch.lower())
    return answer