def solution(n):
    answer = 1
    num = 1
    while answer * (num + 1) <= n:
        num += 1
        answer *= num
    return num
