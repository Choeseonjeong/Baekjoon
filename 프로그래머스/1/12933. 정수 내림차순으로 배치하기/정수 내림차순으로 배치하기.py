def solution(n):
    n = sorted([i for i in str(n)],reverse=True)
    return int(''.join(n))