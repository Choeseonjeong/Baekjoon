def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    s.reverse()
    return "".join(s)