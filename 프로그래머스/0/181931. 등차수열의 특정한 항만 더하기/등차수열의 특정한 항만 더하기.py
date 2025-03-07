def solution(a, d, included):
    arr = []
    sum = a
    answer = 0
    for i in range(len(included)):
        arr.append(sum)
        sum += d
    dic = dict(zip(arr,included))
    for key, values in dic.items():
        if values == True:
            answer+=key
    return answer