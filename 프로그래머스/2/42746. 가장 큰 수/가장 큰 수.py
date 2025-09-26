def solution(numbers):
    answer = ''
    numbers = sorted(list(map(str,numbers)),reverse=True,key=lambda x: x*3)
    for i in numbers:
        answer+=i
    return str(int(answer))