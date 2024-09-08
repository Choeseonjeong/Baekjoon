def solution(name, yearning, photo):
    result=[]
    d = dict(zip(name,yearning))
    for i in photo:
        answer=0
        for j in i:
            if j in d:
                answer+=d[j]
        result.append(answer)
        
    return result