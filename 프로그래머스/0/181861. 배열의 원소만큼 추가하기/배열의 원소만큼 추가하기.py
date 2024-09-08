def solution(arr):
    answer = []
    for idx, val in enumerate(arr):
        for i in range(val):
            answer.append(arr[idx])
    return answer