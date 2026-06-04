def solution(array, commands):
    answer = []
    for com in commands:
        i,j,k = com
        arr = array.copy()
        temp = sorted(arr[i-1:j])
        answer.append(temp[k-1])
    return answer