def solution(s):
    CountSame = 0 
    CountNot = 0
    result = 0
    for i in range(len(s)):
        if CountSame==CountNot:
            temp = s[i]
            result +=1
        if temp == s[i]:
            CountSame+=1
        else:
            CountNot+=1
    return result
