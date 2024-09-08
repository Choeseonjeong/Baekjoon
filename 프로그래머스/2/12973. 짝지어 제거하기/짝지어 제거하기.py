def solution(s):
    a = []
    for i in s:
        if len(a) == 0:
            a.append(i)
        elif a[-1] == i:
            a.pop()
        else:
            a.append(i)
    if len(a) == 0:
        return 1
    else:
        return 0

