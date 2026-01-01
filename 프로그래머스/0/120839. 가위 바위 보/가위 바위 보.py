def solution(rsp):
    answer = ''
    for word in rsp:
        if word == "2":
            answer+="0"
        elif word == "0":
            answer+='5'
        else:
            answer+='2'
    return answer