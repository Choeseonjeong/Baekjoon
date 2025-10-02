def solution(participant, completion):
    dic = dict()
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in completion:
        if j in dic:
            dic[j] -= 1
    answer = []
    for key,value in dic.items():
        if value > 0:
            return key