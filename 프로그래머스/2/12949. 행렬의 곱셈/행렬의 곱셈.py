def solution(arr1, arr2):
    ans = []
    m,n,k = len(arr1),len(arr1[0]),len(arr2[0])
    num = [[0] * k for _ in range(m)]
    
    for a in range(m):
        for b in range(k):
            for c in range(n):
                num[a][b] += arr1[a][c] * arr2[c][b]
    return num