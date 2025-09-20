import math
def solution(progresses, speeds):
    arr = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    result = []
    count = 1
    bepo = arr[0]
    for i in range(1,len(arr)):
        if bepo >= arr[i]:
            count+=1
        else:
            result.append(count)
            count = 1
            bepo = arr[i]
    result.append(count)
    return result