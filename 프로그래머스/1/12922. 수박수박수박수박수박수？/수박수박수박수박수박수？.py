def solution(n):
    ch = ''
    for idx in range(n):
        if idx%2==0:
            ch += "수"
        else:
            ch += "박"
    return ch