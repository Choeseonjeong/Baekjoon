from collections import Counter

def solution(topping):
    left = set()
    right = Counter(topping)
    cnt = 0
    for top in topping:
        left.add(top)
        right[top] -= 1
        
        if right[top] == 0:
            del right[top]
        
        if len(left) ==len(right):
            cnt += 1
    return cnt