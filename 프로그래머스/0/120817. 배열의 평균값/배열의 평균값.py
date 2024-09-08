def solution(numbers):
    n = len(numbers)
    m = 0
    for i in numbers:
        m += i
    return m / n
