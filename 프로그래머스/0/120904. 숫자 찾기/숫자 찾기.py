def solution(num, k):
    answer = 0
    for idx,num in enumerate(str(num)):
        if int(num)==k:
            return idx+1
    return -1 