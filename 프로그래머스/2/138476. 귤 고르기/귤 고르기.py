def solution(k, tangerine):
    budget = {}
    for i in tangerine:
        if i in budget:
            budget[i]+=1
        else:
            budget[i]=1
    a = sorted(budget.items(),key=lambda x : x[1],reverse=True)
    answer = 0
    for j in a:
        x,y = j
        k-=y
        if k<=0:
            break
        else:
            answer+=1
    return answer+1