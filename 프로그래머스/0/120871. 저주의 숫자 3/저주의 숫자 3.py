def solution(n):
    count = 0
    for _ in range(n):
        count += 1
        while count % 3 == 0 or '3' in str(count):
            count += 1
    return count