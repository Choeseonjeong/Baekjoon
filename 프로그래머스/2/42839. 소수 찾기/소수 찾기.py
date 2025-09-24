from itertools import permutations

def solution(numbers):
    def isprime(num):
        if num<2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num%i==0:
                return False
        return True
    
    all = set()
    
    for i in range(1,len(numbers)+1):
        for j in list(map(''.join,permutations(numbers,i))):
            all.add(int(j))
    ans = 0
    for a in all:
        if isprime(a):
            ans+=1
    return ans
        