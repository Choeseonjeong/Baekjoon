def solution(array, commands):
    answer = []
    for n in commands:
        i,j,k = n
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])
    return answer