def solution(participant, completion):
    peoples = dict()
    for i in participant:
        if i not in peoples:
            peoples[i] = 1
        else:
            peoples[i] += 1
    for i in completion:
        peoples[i] -= 1 
        if peoples[i]==0:
            peoples.pop(i)
    answer = ''
    for i in peoples.keys():
        answer+=i
    return answer