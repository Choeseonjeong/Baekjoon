from itertools import permutations

def solution(numbers):
    def isprime(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    num = set()
    count = 0
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            num.add(int(''.join(j)))
    for k in num:
        if isprime(k):
            count+=1
    return count
    