def solution(num, k):
    for idx, word in enumerate(str(num)):
        if int(word) == k:
            return idx+1
    return -1