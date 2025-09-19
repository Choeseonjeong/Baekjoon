def solution(land):
    n,m = len(land),len(land[0])
    for i in range(1,n):
        for j in range(m):
            land[i][j] += max(land[i-1][k] for k in range(m) if k!=j)
    return max(land[-1])