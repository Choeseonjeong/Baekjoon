from itertools import permutations

def solution(numbers):
    def prime(n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    num = []
    for i in range(1,len(numbers)+1):
        num.extend(permutations(numbers,i))
    renum = list(set(map(int,(''.join(i) for i in num))))
    result = []
    for j in renum:
        result.append(prime(j))
    return result.count(True)