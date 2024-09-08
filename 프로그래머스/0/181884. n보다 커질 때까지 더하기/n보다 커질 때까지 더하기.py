def solution(numbers, n):
    answer = 0
    while answer <= n:
        for i in numbers:
            answer+=i
            if answer>n:
                break
    return answer