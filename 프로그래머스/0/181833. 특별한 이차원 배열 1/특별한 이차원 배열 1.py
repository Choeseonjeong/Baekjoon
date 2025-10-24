def solution(n):
    answer = [[0]*n for _ in range(n)]
    for i in range(len(answer)):
        for j in range(len(answer)):
            if i == j:
                answer[i][j] = 1
    return answer