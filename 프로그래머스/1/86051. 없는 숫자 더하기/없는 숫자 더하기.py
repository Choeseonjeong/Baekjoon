def solution(numbers):
    answer = [n for n in range(0,10)]
    result = 0
    for num in answer:
        if num not in numbers:
            result+=num
    return result