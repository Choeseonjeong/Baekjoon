def solution(d, budget):
    answer = []
    d.sort()
    count = 0
    for i in range(len(d)):
        answer.append(d[i])
        if sum(answer)>budget:
            break
        count+=1
    return count