def solution(s):
    arr = []
    for ch in s:
        if not arr:
            arr.append(ch)
        elif arr and ch == '(':
            arr.append(ch)
        elif arr and ch == ')':
            arr.pop()
    return False if arr else True