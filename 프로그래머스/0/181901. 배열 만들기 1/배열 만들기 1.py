def solution(n, k):
    answer = []
    return [i*k for i in range(1,n//k+1)]