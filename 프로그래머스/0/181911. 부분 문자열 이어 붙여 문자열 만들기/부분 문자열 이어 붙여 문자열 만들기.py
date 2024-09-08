def solution(arr, parts):
    answer=''
    for i in range(len(parts)):
        s,e = parts[i]
        num = arr[i]
        answer+=num[s:e+1]
    return answer