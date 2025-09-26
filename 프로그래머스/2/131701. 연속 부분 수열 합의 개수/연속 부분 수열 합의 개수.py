def solution(elements):
    eLen = len(elements)
    element = elements*2
    ans = set()
    
    for i in range(eLen):
        for num in range(1,eLen+1): #  1,2,3,4,5 묶음
            ans.add(sum(element[i:i+num]))
    return len(list(ans))