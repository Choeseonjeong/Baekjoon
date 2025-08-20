def solution(arr, d):
    answer = []
    for i in d:
        x,y = i
        answer+=(arr[x:y+1])
    return answer