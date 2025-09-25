def solution(array, commands):
    answer = []
    for start,end,idx in commands:
        arr = sorted(array[start-1:end])
        answer.append(arr[idx-1])
    return answer