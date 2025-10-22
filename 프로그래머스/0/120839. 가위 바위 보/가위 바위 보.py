def solution(rsp):
    answer = ''
    # 가위는 2 / 바위는 0 / 보는 5
    for word in rsp:
        if word=="2":
            answer += "0"
        elif word=="0":
            answer+="5"
        else:
            answer+="2"
    return answer