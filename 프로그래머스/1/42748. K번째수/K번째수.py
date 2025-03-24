def solution(array, commands):
    answer = []
    arr = []
    for group in commands:
        start, end, index = group
        answer = array[start-1:end]
        answer.sort()
        arr.append(answer[index-1])
    return arr