def solution(arr):
    answer = []
    num = min(arr)

    for i in arr:
        if num != i:
            answer.append(i)
    if answer:
        return answer
    else:
        return [-1]