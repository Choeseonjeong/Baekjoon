def solution(A, B):
    num = len(A)+1
    cnt = 0
    while num > 0:
        if A == B:
            return cnt
        A = A[-1]+A[:-1]
        cnt += 1
        num -= 1
    return -1