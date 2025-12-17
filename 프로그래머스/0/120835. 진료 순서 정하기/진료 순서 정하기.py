def solution(emergency):
    answer = {}
    for idx,num in enumerate(sorted(emergency,reverse=True)):
        answer[num] = idx+1
    result = []
    for i in emergency:
        result.append(answer[i])
    return result