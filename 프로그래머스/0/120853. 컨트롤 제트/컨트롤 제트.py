def solution(s):
    answer = 0
    control = 0
    for num in s.split():
        if num == 'Z':
            answer -= control
        else:
            control = int(num)
            answer += int(num)
    return answer            
            
            