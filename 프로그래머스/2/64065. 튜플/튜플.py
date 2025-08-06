def solution(s):
    answer = []
    for i in s.split("},"):
        answer.append(i.replace("}","").replace("{","").split(","))
    answer.sort(key = len)
    result = []
    for i in answer:
        for j in i:
            if j not in result:
                result.append(j)
    return list(map(int,result))