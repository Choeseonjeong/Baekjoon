def solution(array):
    num = {}
    for i in array:
        if i in num:
            num[i]+=1
        else:
            num[i]=1
            
    answer = -1
    max_count = 0
    multiple = False
    
    for key,value in num.items():
        if value > max_count:
            answer, max_count = key, value
            multiple = False
        elif value == max_count:
            multiple = True
    if multiple:
        return -1
    return answer
    