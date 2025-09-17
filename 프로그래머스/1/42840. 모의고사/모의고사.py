def solution(answers):
    arrs = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    result = []
    for arr in arrs: # a,b,c
        count = 0
        for i in range(len(answers)): 
            if answers[i] == arr[i % len(arr)]:
                count+=1
        result.append(count)
    max_score = max(result)
    return [i+1 for i, score in enumerate(result) if score == max_score]