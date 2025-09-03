def solution(participant, completion):
    people = {}
    for i in participant:
        if i not in people:
            people[i] = 1
        else:
            people[i] += 1
    for j in completion:
        if j in people:
            people[j]-=1
    for key,value in people.items():
        if value != 0:
            return key