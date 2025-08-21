def solution(myString, pat):
    answer = ''
    return myString[:myString.rindex(pat)+len(pat)]