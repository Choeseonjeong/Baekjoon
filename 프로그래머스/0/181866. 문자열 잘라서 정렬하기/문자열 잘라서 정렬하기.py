def solution(myString):
    answer = []
    for ch in myString.split('x'):
        if ch != '':
            answer.append(ch)
    return sorted(answer)