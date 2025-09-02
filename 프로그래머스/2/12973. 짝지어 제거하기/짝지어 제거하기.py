def solution(s):
    arr = []
    for i in s:
        if not arr:
            arr.append(i)
        elif arr[-1]==i:
            arr.pop()
        else:
            arr.append(i)
    return 0 if arr else 1