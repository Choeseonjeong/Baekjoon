def solution(s):
    s = s.split(" ")
    answer = []
    for i in s:
        answer.append(int(i))
    return str(min(answer))+" "+str(max(answer))