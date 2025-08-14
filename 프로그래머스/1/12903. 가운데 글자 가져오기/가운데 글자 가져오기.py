def solution(s):
    answer = len(s)//2
    return s[answer-1]+s[answer] if len(s)%2==0 else s[answer]