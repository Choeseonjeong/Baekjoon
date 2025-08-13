# 2:가위, 0:바위, 5:보
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == "2":
            answer+="0"
        elif i== "0":
            answer+="5"
        else:
            answer+="2"
    return answer