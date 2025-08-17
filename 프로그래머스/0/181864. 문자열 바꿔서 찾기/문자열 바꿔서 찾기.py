def solution(myString, pat):
    answer = 0
    mystring = myString.lower().replace("a","B").replace("b","A")
    return int(pat in mystring)