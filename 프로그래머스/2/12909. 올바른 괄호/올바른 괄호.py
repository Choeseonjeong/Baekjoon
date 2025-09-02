def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append(i)
        elif i==")":
            if not answer:
                return False
            answer.pop()
    return False if answer else True