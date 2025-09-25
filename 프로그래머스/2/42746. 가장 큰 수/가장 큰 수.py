def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = sorted(numbers,key=lambda x:x*6,reverse=True)
    for i in numbers:            
        answer += i
    return str(int(answer))
