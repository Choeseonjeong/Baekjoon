def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        slice_array = array[i - 1 : j]
        sort_slice_array = sorted(slice_array)
        answer.append(sort_slice_array[k - 1])
    return answer
