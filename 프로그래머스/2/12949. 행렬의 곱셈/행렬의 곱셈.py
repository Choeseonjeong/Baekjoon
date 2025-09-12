def solution(arr1, arr2):
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])
    matrix = [[0 for _ in range(r)] for _ in range(m)]
    for i in range(m):
        for j in range(r):
            for k in range(n):
                matrix[i][j] += arr1[i][k] * arr2[k][j]
    return matrix
