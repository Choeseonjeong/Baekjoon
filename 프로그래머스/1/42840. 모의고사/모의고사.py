def solution(answers):
    answer = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    result = []
    for people in answer:
        count = 0
        for i in range(len(answers)):
            if answers[i] == people[i%len(people)]:
                count+=1
        result.append(count)
    return [idx+1 for idx,j in enumerate(result) if j == max(result)]
            