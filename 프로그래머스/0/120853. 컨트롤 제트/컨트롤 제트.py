def solution(s):
    answer = 0
    ex = 0
    for num in s.split(" "):
        if num != "Z":
            ex = int(num) 
            answer += int(num)
        else:
            answer -= ex
    return answer