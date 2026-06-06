def solution(n):
    count = 0
    for a in range(1,n+1):
        total = 0
        for b in range(a, n+1):
            total += b
            if total > n:
                break
            elif total == n:
                count += 1
    return count