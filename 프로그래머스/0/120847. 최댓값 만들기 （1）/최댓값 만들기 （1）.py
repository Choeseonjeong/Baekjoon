def solution(numbers):
    for i in numbers:
        k = sorted(numbers)
        return int(k[-1]) * int(k[-2])
