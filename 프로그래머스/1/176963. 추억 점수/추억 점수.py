def solution(name, yearning, photo):
    dic = {}
    for n,y in zip(name, yearning):
        dic[n] = y
        
    result = []
    for group in photo:
        ans = 0
        for people in group:
            if people in dic:
                ans += dic[people]
            else:
                ans += 0
        result.append(ans)
    return result