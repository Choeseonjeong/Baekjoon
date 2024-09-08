def solution(arr, idx):
    answer = arr[idx:]
    num = 0
    count = answer.count(1)
    if count==0:
        return -1 
    else:
        for i in answer:
            if i != 1:
                num+=1
            else:
                return idx+num