def solution(t, p):
    n = len(p)
    count = 0
    for i in range(len(t)-n+1):
        if int(t[i:i+n]) <= int(p):
            count+=1
    return count
        