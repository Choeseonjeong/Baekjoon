def solution(name, yearning, photo):
    answer = {}
    result = []
    for i in range(len(name)):
        answer[name[i]]=yearning[i]
        
    for group in photo:
        total = 0
        for person in group:
            total += answer.get(person,0)
        result.append(total)
    return result