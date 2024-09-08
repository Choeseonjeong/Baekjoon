def solution(a, b):
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    num = 0
    result = 0
    for i in range(0,a-1):
        num += day[i]
    num+=b
    while num >= 7: 
        num=num-7
        result+=1
    date = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return date[num-1]