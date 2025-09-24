from itertools import combinations

def solution(nums):
    def isprime(num):
        if num < 2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    count = 0
    all = list((sum(i) for i in combinations(nums,3)))
    
    count = 0
    for j in all:
        if isprime(j):
            count+=1
    return count