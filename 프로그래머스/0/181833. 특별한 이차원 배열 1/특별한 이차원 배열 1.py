def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    for num in range(n):
        answer[num][num]+=1
    return answer
    