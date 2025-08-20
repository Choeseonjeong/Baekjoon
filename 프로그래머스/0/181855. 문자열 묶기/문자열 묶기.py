def solution(strArr):    
    strArr = [len(i) for i in strArr]    
    return max(strArr.count(i) for i in range(1, max(strArr) + 1))
