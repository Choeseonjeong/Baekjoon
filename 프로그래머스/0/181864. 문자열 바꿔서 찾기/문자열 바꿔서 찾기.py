def solution(myString, pat):
    answer = 0
    myString = myString.replace('A', 'temp').replace('B', 'A').replace('temp', 'B')
    if pat in myString:
        return 1
    else:
        return 0