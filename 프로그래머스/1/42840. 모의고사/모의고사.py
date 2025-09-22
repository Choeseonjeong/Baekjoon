def solution(answers):
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == people1[i%5] :
            score[0] += 1
        if answers[i] == people2[i%8] :
            score[1] += 1
        if answers[i] == people3[i%10] :
            score[2] += 1
            
    for idx, num in enumerate(score) :
        if num == max(score) :
            answer.append(idx +1)
    
    return answer