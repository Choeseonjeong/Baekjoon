def solution(a, b):
    answer = [31,29,31,30,31,30,31,31,30,31,30,31]
    num = 0
    for i in answer[:a-1]:
        num+=i
    num+=b
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    
    return day[num%7]