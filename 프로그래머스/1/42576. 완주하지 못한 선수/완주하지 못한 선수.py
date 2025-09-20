def solution(participant, completion):
    people = {}
    for i in participant:
        if i in people:
            people[i] += 1
        else:
            people[i] = 1
    for i in completion:
        if i in people:
            people[i]-=1
    result = ''
    for key,value in people.items():
        if value != 0:
            result+=key
    return result