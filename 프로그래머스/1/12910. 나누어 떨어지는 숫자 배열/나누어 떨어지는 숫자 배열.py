def solution(arr, divisor):
    answer = [n for n in arr if n%divisor == 0]
    return sorted(answer) if len(answer) > 0 else [-1]