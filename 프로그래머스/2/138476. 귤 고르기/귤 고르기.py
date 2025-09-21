from collections import Counter

def solution(k, tangerine):
    box = Counter(tangerine)
    counts = sorted(box.values(), reverse=True)
    
    answer = 0
    for i in counts:
        if k <= 0:
            break
        k -= i
        answer+=1
    return answer