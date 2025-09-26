from itertools import permutations
def solution(numbers):
    def isprime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    all = set()
    count = 0
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            all.add(int(''.join(j)))
    for n in all:
        if isprime(n):
            count+=1
    return count