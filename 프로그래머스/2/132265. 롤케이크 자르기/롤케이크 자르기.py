from collections import Counter

def solution(topping):
    num1 = Counter(topping)
    num2 = set()
    count = 0
    
    for i in topping:
        num1[i] -= 1
        num2.add(i)
            
        if num1[i] == 0:
            num1.pop(i)
            
        if len(num1)==len(num2):
            count+=1
    return count