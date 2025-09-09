def solution(want, number, discount):
    shop = {}
    for i,j in zip(want, number):
        shop[i] = j 
    result = 0
    num = len(discount)-9
    
    for i in range(num): 
        arr = discount[i:i+10]
        for a in want:
            if shop[a]>arr.count(a):
                break
        else:
            result+=1
    return result