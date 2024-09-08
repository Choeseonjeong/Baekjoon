def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i:])
    return sorted(answer)