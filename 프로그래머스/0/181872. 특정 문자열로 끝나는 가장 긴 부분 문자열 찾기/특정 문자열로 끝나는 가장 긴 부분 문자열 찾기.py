def solution(myString, pat):
    answer = ''
    num = myString.rfind(pat)
    answer += myString[0:num+len(pat)]
    return answer