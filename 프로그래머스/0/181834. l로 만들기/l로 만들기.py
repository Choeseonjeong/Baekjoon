def solution(myString):
    answer = ''
    for word in myString:
        if word in ['a','b','c','d','e','f','g','h','i','j','k']:
            answer+='l'
        else:
            answer+=word
    return answer