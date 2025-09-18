from itertools import permutations

def sosu(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True    


def solution(numbers):
    num = []
    answer = 0
    
    for i in range(1,len(numbers)+1): # 순열 
        num.extend(permutations(numbers,i))
        
    candidates = set(int(''.join(p)) for p in num)
        
    for i in candidates:
        if sosu(i):
            answer+=1
    return answer
            