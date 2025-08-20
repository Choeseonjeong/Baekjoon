def solution(myString, pat):
    answer = []
    num = len(pat)
    for i in range(len(myString)-num+1):
        answer.append(myString[i:i+num])
    return answer.count(pat)