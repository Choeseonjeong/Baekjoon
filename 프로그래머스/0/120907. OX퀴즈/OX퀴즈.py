def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split("=")
        if eval(i[0]) == int(i[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer