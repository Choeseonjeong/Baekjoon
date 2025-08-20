def solution(numbers, n):
    answer = 0
    idx = 0
    while n>=answer:
        answer+=numbers[idx]
        idx+=1
    return answer