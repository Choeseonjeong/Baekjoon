def solution(s, skip, index):
    arr = 'abcdefghijklmnopqrstuvwxyz'
    answer =''
    arr2 = []
    for i in list(arr):
        if i not in skip:
            arr2.append(i)
            
    for j in s:
        idx = (arr2.index(j)+index)%len(arr2)
        answer += arr2[idx]

    return answer