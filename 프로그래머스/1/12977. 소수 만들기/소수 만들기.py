from itertools import combinations
def solution(nums):
    answer = set()
    count = 0
    def isprime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5+1)):
            if n%i==0:
                return False
        return True

    for i in combinations(nums,3):
        answer.add(i)
    for i in list(answer):
        if isprime(sum(i)):
            count += 1
    return count