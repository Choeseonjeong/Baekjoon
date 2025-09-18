def solution(genres, plays):
    dic1 = dict()
    dic2 = dict()
    for i,(g,p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [[i,p]]
        else:
            dic1[g].append([i,p])
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    result = []
    for (g,p) in sorted(dic2.items() ,key = lambda x: x[1],reverse=True):
        for (i,p) in sorted(dic1[g], key = lambda x: x[1], reverse=True)[:2]:
            result.append(i)
    return result