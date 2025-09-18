def solution(genres, plays):
    dic1 = dict()
    dic2 = dict()
    result = []
    for idx, (g,p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(idx,p)]
        else:
            dic1[g].append((idx,p))
    for (g,p) in zip(genres, plays):
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    
    for (ge,pl) in sorted(dic2.items(),key=lambda x: x[1],reverse=True):
        for (i,pla) in sorted(dic1[ge],key=lambda x: x[1],reverse=True)[:2]:
            result.append(i)
    return result
        
        
        