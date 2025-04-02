def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(0,len(score)//m*m,m):
         answer += score[i + m - 1] * m
    return answer
