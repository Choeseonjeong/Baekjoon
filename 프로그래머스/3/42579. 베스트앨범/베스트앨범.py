def solution(genres, plays):
    dic1 = dict()
    dic2 = dict()
    answer = []
    
    for g,p in zip(genres, plays):
        if g in dic1:
            dic1[g] += p
        else:
            dic1[g] = p
    for idx,(g,p) in enumerate(zip(genres, plays)):
        if g in dic2:
            dic2[g] += [[p,idx]]
        else:
            dic2[g] = [[p,idx]]
            
    for (k,v) in sorted(dic1.items(), key=lambda x: x[1], reverse=True):
        for (i,j) in sorted(dic2[k],reverse=True,key=lambda x: x[0])[:2]:
            answer.append(j)
    return answer