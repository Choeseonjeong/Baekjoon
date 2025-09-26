from collections import Counter

def solution(topping):
    old = Counter(topping)
    young = set()
    count = 0
    
    for num in topping:
        old[num] -= 1
        young.add(num)
        if old[num]==0:
            old.pop(num)
        if len(old) == len(young):
            count+=1
    return count