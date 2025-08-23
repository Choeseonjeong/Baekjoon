def solution(score):
    people = [sum(i)/2 for i in score]
    student = sorted(people, reverse=True)
    result = []
    for i in people:
        result.append(student.index(i)+1)
    return result