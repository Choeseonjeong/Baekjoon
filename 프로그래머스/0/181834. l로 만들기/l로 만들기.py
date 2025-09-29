def solution(myString):
    answer = 'abcdefghijk'
    ch = ''
    for i in myString:
        if i in answer:
            ch+="l"
        else:
            ch+=i
    return ch