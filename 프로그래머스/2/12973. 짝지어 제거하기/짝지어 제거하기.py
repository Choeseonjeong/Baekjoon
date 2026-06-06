def solution(s):
    arr = []
    for ch in s:
        if not arr:
            arr.append(ch)
        elif arr and arr[-1] == ch:
            arr.pop()
        elif arr and arr[-1] != ch:
            arr.append(ch)
    return 0 if arr else 1