def solution(t, p):
    plen = len(p)
    arr = []
    for i in range(len(t)-plen+1):
        arr.append(t[i:i+plen])
    answer = 0
    for i in arr:
        if int(i) <= int(p):
            answer+=1
    return answer